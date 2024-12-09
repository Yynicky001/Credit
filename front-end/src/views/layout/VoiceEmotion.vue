<template>
  <div class="voice-emotion">
    <h2>声音情绪识别</h2>
    <MessagePopup :message="message"/>
    <div>
      <audio ref="audio" id="audioPlayer" controls style="display: none;">
        <source id="audioSource" type="audio/wav">
        您的浏览器不支持音频元素。
      </audio>
     <div class="audio-icon" ref="audioIcon">
      <i class="fas fa-volume-up"></i>
     </div>
     <div class="recording-icon" v-if="isRecording">
      <i class="fas fa-microphone"></i>
      <div class="progress-bar" :style="{ width: progress + '%' }"></div>
    </div>
    </div>
    <div>
      <div class="recording-container" >
        <div class="recording-text" v-for ="index in 5" :key="index">
            <span class="question-text">第{{ index }}个问题</span>
            <button @click="startSound( index )" id="playAudioBtn" title="播放音频">
              <img src="../../assets/images/播放.png" class="play-img"/>
            </button>
            <button @click="startRecording(index)" id="recordAudioBtn" title="开始录音">
              <img src="../../assets/images/mic-on.png" class="play-img"/>
            </button>
            <button @click="reset(index)" id="resetBtn" title="重置">
              <img src="../../assets/images/reset.png" class="play-img"/>
            </button>
            <AudioVisualizer style="width: 790px;height: 50px"/>
        </div>
      </div>
    </div>
    <div id="EmotionAnalysis" >
      <EmotionAnalysis :DataDip="Datavoice" :resultdata="resultdata" style="width: 600px;height: 240px;"/>
    <div class="container">
    <!-- Waveform display -->
    <!-- Emotion recognition -->
    <div id="emotion" class="emotion"></div>
    <!-- Credit score -->
    <div id="score" class="score"></div>
    </div>
    </div>
</div>
</template>
<script>
import * as echarts from 'echarts'
import EmotionAnalysis from '@/components/EmotionAnalysis.vue'
import _ from 'lodash'
import AudioVisualizer from '@/components/AudioVisualizer.vue'
import MessagePopup from '@/components/MessagePopup.vue'

export default {
  components: {
    EmotionAnalysis,
    AudioVisualizer,
    MessagePopup
  },
  data () {
    return {
      Datavoice: '声音情绪',
      audio: null,
      resultdata: [],
      number1: 1,
      number2: 1,
      dataListTemp: [],
      dataListTemp1: [0, 0, 0, 0, 0, 0],
      blob: null,
      isRecording: false,
      progress: 0,
      timer: null,
      message: '! 请先点击播放，再点击录音，完成后可显示分析结果'
    }
  },
  methods: {
    // 声音播放
    startSound (index) {
      console.log('playAudio' + index)
      this.playAudio(index)
      // 声音播放控制
      const audio = this.$refs.audio
      const audioIcon = this.$refs.audioIcon
      audio.addEventListener('play', () => {
        audioIcon.style.display = 'block'
      })

      audio.addEventListener('pause', () => {
        audioIcon.style.display = 'none'
      })
      audio.addEventListener('timeupdate', () => {
        const progress = (audio.currentTime / audio.duration) * 110
        audioIcon.style.background = `linear-gradient(to right, rgba(255, 255, 255, 1) ${progress}%, rgba(255, 255, 255, 0) 0%)`
      })
    },
    // 音频播放
    async playAudio (index) {
      try {
        const response = await fetch('http://127.0.0.1:5000/get_audio?index=' + index)
        this.blob = await response.blob([ArrayBuffer], { type: 'audio/wav' })
        const url = URL.createObjectURL(this.blob)
        const audioSource = document.getElementById('audioSource')
        const audioPlayer = document.getElementById('audioPlayer')

        audioSource.src = url
        audioPlayer.load()
        audioPlayer.play()
        audioPlayer.onended = () => {
        }
      } catch (error) {
        document.getElementById('audioPlayer').pause()
        console.error('音频加载失败: ', error)
      }
    },
    // 开始录音并识别
    async  startRecording (index) {
      this.statusrecording = '(第' + (this.number2) + '次录音中)'
      console.log('startRecording')
      this.startRecordingIcon()
      const response = await fetch('http://127.0.0.1:5000/predict_emotion', {
        method: 'POST'
      })
      const data = await response.json()
      console.log(data)
      this.resultdata.push(data)
      this.statusrecording = ''
    },
    // 重新回答
    reset (index) {
      this.resultdata = []
      this.dataList = []
      this.dataListTemp1 = [0, 0, 0, 0, 0, 0]
    },
    // 录音图标动画
    startRecordingIcon () {
      this.isRecording = true
      this.progress = 0
      this.timer = setInterval(() => {
        this.progress++
        if (this.progress >= 100) {
          clearInterval(this.timer)
          this.isRecording = false
        }
      }, 50)// 每 50 毫秒增加进度，5 秒达到 100%
    },
    // 响应json数据转换整理
    getData () {
      const newdataList = this.resultdata.map((item) => {
        const newObj = {}
        newObj.name = item.emotion
        newObj.value = item.credit_score
        return newObj
      })
      const groupedData = _.groupBy(newdataList, 'name')
      this.dataListTemp = _.map(groupedData, (group) => {
        const sum = _.sumBy(group, 'value')
        const average = sum / group.length
        return { name: group[0].name, value: average }
      })
      return this.dataListTemp
    },
    getDataCredit_score () {
      this.dataListTemp.forEach((item) => {
        if (item.name === 'angry') {
          this.dataListTemp1[0] = item.value
        }
        if (item.name === 'happy') {
          this.dataListTemp1[1] = item.value
        }
        if (item.name === 'neutral') {
          this.dataListTemp1[2] = item.value
        }
        if (item.name === 'sad') {
          this.dataListTemp1[3] = item.value
        }
        if (item.name === 'fearful') {
          this.dataListTemp1[4] = item.value
        }
        if (item.name === 'surprise') {
          this.dataListTemp1[5] = item.value
        }
      })
      console.log(this.dataListTemp1)
      return this.dataListTemp1
    },
    // 绘制饼图
    drawPieChart () {
      // Emotion recognition visualization
      const emotionChart = echarts.init(document.getElementById('emotion'))
      const emotionOption = {
        title: {
          text: '情绪识别',
          left: 'center',
          textStyle: { color: '#ffffff' }
        },
        tooltip: {
          trigger: 'item'
        },
        series: [
          {
            center: ['50%', '60%'],
            name: '情绪',
            type: 'pie',
            radius: '60%',
            data: this.getData(),
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            },
            itemStyle: {
              color: function (params) {
                const colorList = ['#FF4500', '#FFD700', '#32CD32', '#1E90FF', '#9400D3', '#940000']
                return colorList[params.dataIndex]
              }
            }
          }
        ]
      }
      emotionChart.setOption(emotionOption)
    },
    // 绘制柱状图
    drawBarChart () {
      // Credit score visualization
      const scoreChart = echarts.init(document.getElementById('score'))
      const scoreOption = {
        title: {
          text: '情绪对应积分',
          left: 'center',
          textStyle: { color: '#ffffff' }
        },
        tooltip: {},
        xAxis: {
          type: 'category',
          data: ['Angry', 'Happy', 'Neutral', 'Sad', 'Fearful', 'Surprise'],
          axisLine: { lineStyle: { color: '#ffffff' } },
          axisLabel: { color: '#ffffff', fontSize: 8 }
        },
        yAxis: {
          type: 'value',
          axisLine: { lineStyle: { color: '#ffffff' } },
          axisLabel: { color: '#ffffff' }
        },
        grid: {
          top: '13%',
          bottom: '10%',
          left: '10%',
          right: '6%'
        },
        series: [{
          data: this.getDataCredit_score(),
          type: 'bar',
          itemStyle: {
            color: function (params) {
              const scoreColor = ['#FF4500', '#FFD700', '#32CD32', '#1E90FF', '#9400D3', '#940000']
              return scoreColor[params.dataIndex]
            }
          }
        }]
      }
      scoreChart.setOption(scoreOption)
    }
  },
  mounted () {
    this.drawPieChart()
    this.drawBarChart()
    this.$watch('resultdata', function (newVal, oldVal) {
      this.drawPieChart()
      this.drawBarChart()
    })
  }
}
</script>

<style scoped>
.recording-icon {
  position: fixed;
  top: 5%;
  left: 50%;
  width: 200px;
  height: 150px;
  background-color: #6d6d6d5a;
  padding: 10px;
  font-size: 100px;
  color: rgb(110, 110, 110);
  border-radius: 20px;
}

.progress-bar {
  height: 5px;
  background-color: rgb(255, 255, 255);
  transition: width 0.1s ease-in-out;
  border-radius: 10px;
}
.audio-icon {
  position: fixed;
  display : none;
  top: 5%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 9999;
  width: 200px;
  height: 10px;
  font-size: 120px;
  color: rgb(110, 110, 110);
  pointer-events: none;
  border-radius: 20px
}
#playAudioBtn, #recordAudioBtn, #resetBtn {
  margin-right:20px;
  width: 48px;
  height: 48px;
  border-radius: 5px;
  background-color: rgba(60, 87, 145, 0);
  border: none;
  padding: 0px;
  cursor: pointer;
}
.voice-emotion{
    font-family: Arial, sans-serif;
    background-color: rgb(32, 46, 77);
    color: #ffffff;
    text-align: center;
}
.container {
    display: flex;
    /* justify-content: space-around; */
    margin-left: 10px;
}
.waveform, .emotion, .score {
    width: 258px;
    height: 222px;
    padding: 8px;
    margin-left: 10px;
    background-color: rgba(43, 62, 80, 0.9);
    border-radius: 10px;
    box-shadow: 0px 0px 15px rgba(0, 255, 255, 0.5);
}
h2 {
    margin-bottom: 20px;
}
.recording-container {
    max-height: 240px; /* 设置容器的最大高度*/
    overflow-y: auto; /* 出现垂直滚动条 */
    scrollbar-width: none; /* 隐藏滚动条 */
    -ms-overflow-style: none;
    width: 1153px;
    height: 250px;
    padding: 10px;
    margin: 0px;
    background-color: rgba(43, 62, 80, 0.9);
    border-radius: 10px;
    box-shadow: 0px 0px 20px rgba(0, 255, 255, 0.5);
}
#EmotionAnalysis {
  display: flex;
  margin-top: 20px;
}
.recording-text {
  height: 50px;
  display: flex;
  margin-bottom: 10px;
  background-color: rgba(51, 75, 96, 0.9);
}
.question-text {
  padding-left: 15px;
  width: 100px;
  height: 50px;
  line-height: 50px;
  text-align: center;
  font-size: 16px;
  color: #ffffff;
  background-color: rgba(60, 87, 145, 0);
  margin-right: 20px;
}
.play-img {
  width: 45px;
  height: 48px;
}
</style>
