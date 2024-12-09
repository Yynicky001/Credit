import time
import cv2
import tensorflow as tf
import numpy as np
import os
import asyncio
import websockets
import json
import threading
import queue  # 导入队列模块

# 定义情绪列表和分数映射
EMOTIONS = ["angry", "disgusted", "fearful", "happy", "sad", "surprised", "neutral"]
key_table = {
    "angry": 400,
    "disgusted": 500,
    "fearful": 550,
    "happy": 850,
    "neutral": 750,
    "sad": 650,
    "surprised": 750,
}

# 获取文件绝对路径
def get_absolute_path_with_slash(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_file_path = os.path.join(current_dir, file_name)
    target_file_path_with_slash = target_file_path.replace("\\", "/")
    return target_file_path_with_slash

# 加载TensorFlow模型
model = tf.keras.models.load_model("./facial_expression_hybrid_model.h5")

# 加载OpenCV人脸检测模型
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# WebSocket 服务器地址和端口
WEBSOCKET_HOST = "localhost"
WEBSOCKET_PORT = 8765

# 全局变量，用于存储从摄像头获取的帧
frame_buffer = queue.Queue()

# 用于捕获视频的线程函数
def capture_video():
    global frame_buffer
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("无法打开摄像头")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法获取摄像头数据")
            break

        # 将捕获的帧放入队列中
        if frame_buffer.qsize() < 10:  # 防止队列无限堆积
            frame_buffer.put(frame)

    cap.release()

# WebSocket 事件处理
async def emotion_detection(websocket, path):
    predictions = []
    scores = []
    start_time = time.time()

    try:
        while True:
            # 从队列中获取最新的帧
            if not frame_buffer.empty():
                frame = frame_buffer.get()  # 从队列中取出最新的帧
            else:
                await asyncio.sleep(0.1)  # 如果没有帧，休眠一下再试
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            result_data = {}
            if len(faces) > 0:
                x, y, w, h = faces[0]  # 只识别第一个人脸
                face_roi = gray[y:y+h, x:x+w]
                face_roi = cv2.resize(face_roi, (64, 64))
                face_roi = np.repeat(face_roi[..., np.newaxis], 3, axis=-1)  # 转换为三通道
                face_roi = np.expand_dims(face_roi, axis=0) / 255.0  # 归一化

                prediction = model.predict(face_roi)
                prediction = np.array(prediction[0])  # 确保我们获得的是一维数组
                predictions.append(prediction)

                emotion_index = np.argmax(prediction)
                emotion_text = EMOTIONS[emotion_index]

                # 获取当前情绪的分数并存储
                score = key_table[emotion_text]
                scores.append(score)

                # 记录结果数据
                result_data = {
                    "emotion": emotion_text,
                    "score": score,  
                }

                # 在图像上绘制情绪标签
                cv2.putText(frame, f"Emotion: {emotion_text}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                cv2.putText(frame, f"Score: {score}", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                # 将数据发送给前端
                await websocket.send(json.dumps(result_data))

            # 计算平均值并输出到终端
            elapsed_time = time.time() - start_time
            if elapsed_time >= 4:
                avg_prediction = np.mean(predictions, axis=0)
                avg_emotion_index = np.argmax(avg_prediction)
                avg_emotion_text = EMOTIONS[avg_emotion_index]
                avg_score = np.mean(scores)

                print(f"4秒平均情绪: {avg_emotion_text} - 平均分数: {avg_score:.2f}")

                # 将平均值发送给前端
                avg_result_data = {
                    "average_emotion": avg_emotion_text,
                    "average_score": avg_score,
                }
                await websocket.send(json.dumps(avg_result_data))

                predictions.clear()
                scores.clear()
                start_time = time.time()

            # 按帧显示
            cv2.imshow("Emotion Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    except websockets.ConnectionClosed:
        print("客户端断开连接")
    finally:
        pass

# 启动 WebSocket 服务器
async def main():
    async with websockets.serve(emotion_detection, WEBSOCKET_HOST, WEBSOCKET_PORT):
        print(f"WebSocket 服务器已启动: ws://{WEBSOCKET_HOST}:{WEBSOCKET_PORT}")
        await asyncio.Future()  # 保持服务器运行

# 主程序
if __name__ == "__main__":
    # 启动视频捕获线程
    threading.Thread(target=capture_video, daemon=True).start()
    # 启动 WebSocket 服务器
    asyncio.run(main())
