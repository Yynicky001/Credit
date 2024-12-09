from flask import Flask, jsonify, request
from keras.models import load_model
from flask_cors import CORS
import numpy as np
import librosa
import pyaudio
import pymysql
import wave
import os
from flask import Flask, send_file

app = Flask(__name__)
CORS(app)

# 获取文件绝对路径
def get_absolute_path_with_slash(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_file_path = os.path.join(current_dir, file_name)
    # 将路径中的\替换成/
    target_file_path_with_slash = target_file_path.replace("\\", "/")
    return target_file_path_with_slash

# 获取同一文件夹下名为voice.keras的文件路径
voice_file_name = "voice.keras"
voice_absolute_path_with_slash = get_absolute_path_with_slash(voice_file_name)
print("指定文件的绝对路径（路径分隔符为/）是:", voice_absolute_path_with_slash)
# 加载情绪识别模型
emotions = ["angry", "fear", "happy", "neutral", "sad", "surprise"]
model = load_model(voice_absolute_path_with_slash)
# 情绪和信用评分的映射表
key_table = {
    "angry": 400,
    "fear": 550,
    "happy": 850,
    "neutral": 750,
    "sad": 650,
    "surprise": 750,
}

tar_len = 108784  # 目标音频长度

# 音频预处理函数
def preprocess_audio(file_path):
    audio, sample_rate = librosa.load(file_path, sr=16000)
    factor = len(audio) / tar_len
    audio = librosa.effects.time_stretch(audio, rate=factor)

    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_processed = np.expand_dims(mfccs.T, axis=0)
    return mfccs_processed

# 录音函数
def record_audio(time=5, save_file="test.wav"):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = time

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    
    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(save_file, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))

# Flask 路由处理
@app.route('/predict_emotion', methods=['POST'])
def predict_emotion():
	
    # 开始录音并保存
    file_path = "test.wav"
    record_audio(save_file=file_path)
    
    # 处理录音并预测情绪
    audio_data = preprocess_audio(file_path)
    predictions = model.predict(audio_data)
    os.remove(file_path)  # 删除临时文件

    # 确定情绪并映射信用积分
    predicted_class = np.argmax(predictions, axis=1)[0]
    predicted_emotion = emotions[predicted_class]
    credit_score = key_table.get(predicted_emotion, "N/A")

    # 返回 JSON 响应
    return jsonify({"emotion": predicted_emotion, "credit_score": credit_score})

# 获取音频
@app.route('/get_audio', methods=['GET'])
def get_audio():
    #接收参数index
    index = request.args.get('index',default=1)
    # 替换成你的文件路径
    file_path = "voice_question/"+"text"+str(index)+".wav"
    return send_file(file_path, mimetype='audio/wav')
@app.route('/sendFormDatajson', methods=['POST'])
def receive_json():
    json_data = request.get_json()
    if json_data:
        print(json_data)
        return jsonify([{"option": "操作1", "name": "张三", "username": "zhangsan", "sex": "男", "credit_score": 70,"remark": "备注1"}, {"option": "操作2", "name": "李四", "username": "lisi", "sex": "女", "credit_score": 80,"remark": "备注2"}])
    return jsonify({})
# 查询用户数据并且插入备注
@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    username = data.get('username')
    chinese_string = data.get('remark')
    # 连接数据库
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        database='competition1'
    )
    try:
        with connection.cursor() as cursor:
            # 先执行插入操作
            insert_sql = "INSERT INTO loan_user (remark) VALUES (%s)"
            cursor.execute(insert_sql, (chinese_string,))
            connection.commit()

            # 再执行查询操作
            sql = "SELECT * FROM loan_user WHERE username=%s"
            cursor.execute(sql,(username,))
            # 获取查询结果并转换为字典列表形式，以便转换为JSON格式
            results = cursor.fetchall()
            print(1111)
            columns = [col[0] for col in cursor.description]
            result_list = [dict(zip(columns, row)) for row in results]
            print(result_list)
        return jsonify(result_list)
    except Exception as e:
        print("发生错误:", e)
        return jsonify({"error": str(e)}), 500
    finally:
        # 关闭连接
        connection.close()
        
if __name__ == "__main__":
    app.run(debug=True)
    