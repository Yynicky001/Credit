skeleton_map = [
    {
        "srt_kpt_id": 15,
        "dst_kpt_id": 13,
        "color": [0, 100, 255],
        "thickness": 2,
    },  # 右侧脚踝-右侧膝盖
    {
        "srt_kpt_id": 13,
        "dst_kpt_id": 11,
        "color": [0, 255, 0],
        "thickness": 2,
    },  # 右侧膝盖-右侧胯
    {
        "srt_kpt_id": 16,
        "dst_kpt_id": 14,
        "color": [255, 0, 0],
        "thickness": 2,
    },  # 左侧脚踝-左侧膝盖
    {
        "srt_kpt_id": 14,
        "dst_kpt_id": 12,
        "color": [0, 0, 255],
        "thickness": 2,
    },  # 左侧膝盖-左侧胯
    {
        "srt_kpt_id": 11,
        "dst_kpt_id": 12,
        "color": [122, 160, 255],
        "thickness": 2,
    },  # 右侧胯-左侧胯
    {
        "srt_kpt_id": 5,
        "dst_kpt_id": 11,
        "color": [139, 0, 139],
        "thickness": 2,
    },  # 右边肩膀-右侧胯
    {
        "srt_kpt_id": 6,
        "dst_kpt_id": 12,
        "color": [237, 149, 100],
        "thickness": 2,
    },  # 左边肩膀-左侧胯
    {
        "srt_kpt_id": 5,
        "dst_kpt_id": 6,
        "color": [152, 251, 152],
        "thickness": 2,
    },  # 右边肩膀-左边肩膀
    {
        "srt_kpt_id": 5,
        "dst_kpt_id": 7,
        "color": [148, 0, 69],
        "thickness": 2,
    },  # 右边肩膀-右侧胳膊肘
    {
        "srt_kpt_id": 6,
        "dst_kpt_id": 8,
        "color": [0, 75, 255],
        "thickness": 2,
    },  # 左边肩膀-左侧胳膊肘
    {
        "srt_kpt_id": 7,
        "dst_kpt_id": 9,
        "color": [56, 230, 25],
        "thickness": 2,
    },  # 右侧胳膊肘-右侧手腕
    {
        "srt_kpt_id": 8,
        "dst_kpt_id": 10,
        "color": [0, 240, 240],
        "thickness": 2,
    },  # 左侧胳膊肘-左侧手腕
    {
        "srt_kpt_id": 1,
        "dst_kpt_id": 2,
        "color": [224, 255, 255],
        "thickness": 2,
    },  # 右边眼睛-左边眼睛
    {
        "srt_kpt_id": 0,
        "dst_kpt_id": 1,
        "color": [47, 255, 173],
        "thickness": 2,
    },  # 鼻尖-左边眼睛
    {
        "srt_kpt_id": 0,
        "dst_kpt_id": 2,
        "color": [203, 192, 255],
        "thickness": 2,
    },  # 鼻尖-左边眼睛
    {
        "srt_kpt_id": 1,
        "dst_kpt_id": 3,
        "color": [196, 75, 255],
        "thickness": 2,
    },  # 右边眼睛-右边耳朵
    {
        "srt_kpt_id": 2,
        "dst_kpt_id": 4,
        "color": [86, 0, 25],
        "thickness": 2,
    },  # 左边眼睛-左边耳朵
    {
        "srt_kpt_id": 3,
        "dst_kpt_id": 5,
        "color": [255, 255, 0],
        "thickness": 2,
    },  # 右边耳朵-右边肩膀
    {
        "srt_kpt_id": 4,
        "dst_kpt_id": 6,
        "color": [255, 18, 200],
        "thickness": 2,
    },  # 左边耳朵-左边肩膀
]
bbox_labelstr = {
    "font_size": 6,  # 字体大小
    "font_thickness": 14,  # 字体粗细
    "offset_x": 0,  # X 方向，文字偏移距离，向右为正
    "offset_y": -80,  # Y 方向，文字偏移距离，向下为正
}

# 关键点 BGR 配色
kpt_color_map = {
    0: {"name": "Nose", "color": [0, 0, 255], "radius": 6},  # 鼻尖
    1: {"name": "Right Eye", "color": [255, 0, 0], "radius": 6},  # 右边眼睛
    2: {"name": "Left Eye", "color": [255, 0, 0], "radius": 6},  # 左边眼睛
    3: {"name": "Right Ear", "color": [0, 255, 0], "radius": 6},  # 右边耳朵
    4: {"name": "Left Ear", "color": [0, 255, 0], "radius": 6},  # 左边耳朵
    5: {"name": "Right Shoulder", "color": [193, 182, 255], "radius": 6},  # 右边肩膀
    6: {"name": "Left Shoulder", "color": [193, 182, 255], "radius": 6},  # 左边肩膀
    7: {"name": "Right Elbow", "color": [16, 144, 247], "radius": 6},  # 右侧胳膊肘
    8: {"name": "Left Elbow", "color": [16, 144, 247], "radius": 6},  # 左侧胳膊肘
    9: {"name": "Right Wrist", "color": [1, 240, 255], "radius": 6},  # 右侧手腕
    10: {"name": "Left Wrist", "color": [1, 240, 255], "radius": 6},  # 左侧手腕
    11: {"name": "Right Hip", "color": [140, 47, 240], "radius": 6},  # 右侧胯
    12: {"name": "Left Hip", "color": [140, 47, 240], "radius": 6},  # 左侧胯
    13: {"name": "Right Knee", "color": [223, 155, 60], "radius": 6},  # 右侧膝盖
    14: {"name": "Left Knee", "color": [223, 155, 60], "radius": 6},  # 左侧膝盖
    15: {"name": "Right Ankle", "color": [139, 0, 0], "radius": 6},  # 右侧脚踝
    16: {"name": "Left Ankle", "color": [139, 0, 0], "radius": 6},  # 左侧脚踝
}

# 点类别文字
kpt_labelstr = {
    "font_size": 4,  # 字体大小
    "font_thickness": 10,  # 字体粗细
    "offset_x": 0,  # X 方向，文字偏移距离，向右为正
    "offset_y": 150,  # Y 方向，文字偏移距离，向下为正
}
