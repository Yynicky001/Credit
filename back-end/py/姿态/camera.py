import cv2
import torch
from ultralytics import YOLO
import asyncio
import websockets
import json
import os
import sys

# 获取文件绝对路径
def get_absolute_path_with_slash(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_file_path = os.path.join(current_dir, file_name)
    target_file_path_with_slash = target_file_path.replace("\\", "/")
    return target_file_path_with_slash

# 导入配置文件
CONFIG_PATH = get_absolute_path_with_slash("config.py")
sys.path.append(os.path.dirname(CONFIG_PATH))
import config

# 模型路径
MODEL_PATH = get_absolute_path_with_slash("yolo11x-pose.pt")

# 初始化 YOLO 模型
model = YOLO(MODEL_PATH)

# WebSocket 服务器地址和端口
WEBSOCKET_HOST = "localhost"
WEBSOCKET_PORT = 8765

# 摄像头置信度阈值
CONFIDENCE_THRESHOLD = getattr(config, "CONFIDENCE_THRESHOLD", 0.5)

async def pose_detection(websocket, path):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video stream from camera.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to read frame from camera.")
                break

            # YOLO 推理
            results = model(frame)
            if not results or len(results[0].keypoints.data) == 0:
                continue  # 没有检测到姿态跳过

            # 获取关键点和边框信息
            bboxes_keypoints = results[0].keypoints.data.cpu().numpy()
            num_bbox = len(results[0].boxes.cls)

            result_data = []

            for idx in range(num_bbox):
                bbox_keypoints = bboxes_keypoints[idx]

                # 骨架连接信息
                skeleton_data = []
                for skeleton in config.skeleton_map:
                    srt_kpt_id = skeleton["srt_kpt_id"]
                    dst_kpt_id = skeleton["dst_kpt_id"]

                    # 起点和终点信息
                    srt_kpt_x, srt_kpt_y, srt_kpt_conf = bbox_keypoints[srt_kpt_id]
                    dst_kpt_x, dst_kpt_y, dst_kpt_conf = bbox_keypoints[dst_kpt_id]

                    if srt_kpt_conf > CONFIDENCE_THRESHOLD and dst_kpt_conf > CONFIDENCE_THRESHOLD:
                        skeleton_data.append({
                            "start": [int(srt_kpt_x), int(srt_kpt_y)],
                            "end": [int(dst_kpt_x), int(dst_kpt_y)],
                            "color": skeleton["color"],
                            "thickness": skeleton["thickness"]
                        })

                # 关键点信息
                keypoints_data = []
                for kpt_id, kpt_info in config.kpt_color_map.items():
                    kpt_x, kpt_y, kpt_conf = bbox_keypoints[kpt_id]
                    if kpt_conf > CONFIDENCE_THRESHOLD:
                        keypoints_data.append({
                            "position": [int(kpt_x), int(kpt_y)],
                            "radius": kpt_info["radius"],
                            "color": kpt_info["color"]
                        })

                result_data.append({
                    "skeleton": skeleton_data,
                    "keypoints": keypoints_data
                })

            # 将数据发送到前端
            await websocket.send(json.dumps({
                "frame_data": result_data
            }))

            # 显示结果
            for data in result_data:
                # 绘制骨架
                for skeleton in data["skeleton"]:
                    frame = cv2.line(
                        frame,
                        tuple(skeleton["start"]),
                        tuple(skeleton["end"]),
                        color=skeleton["color"],
                        thickness=skeleton["thickness"]
                    )

                # 绘制关键点
                for keypoint in data["keypoints"]:
                    frame = cv2.circle(
                        frame,
                        tuple(keypoint["position"]),
                        keypoint["radius"],
                        keypoint["color"],
                        -1
                    )

            cv2.imshow("Pose Detection", frame)

            # 按 'q' 键退出
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    except websockets.ConnectionClosed:
        print("客户端断开连接")
    finally:
        cap.release()
        cv2.destroyAllWindows()

# 启动 WebSocket 服务器
async def main():
    async with websockets.serve(pose_detection, WEBSOCKET_HOST, WEBSOCKET_PORT):
        print(f"WebSocket 服务器已启动: ws://{WEBSOCKET_HOST}:{WEBSOCKET_PORT}")
        await asyncio.Future()  # 保持服务器运行

if __name__ == "__main__":
    asyncio.run(main())
