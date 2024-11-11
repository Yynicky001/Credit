<template>
  <div class="voice-emotion">
    <h2>声音情绪识别</h2>
    <button @click="startSound()" style="margin-right:20px;width: 200px;height: 30px;border-radius: 20px;">播放声音{{ statussound }}</button>
    <button @click="startRecording()" style="width: 200px;height: 30px;border-radius: 20px;">开始录音并识别{{ statusrecording }}</button>
  <div class="container">
    <!-- Waveform display -->
    <div id="waveform" class="waveform"></div>

    <!-- Emotion recognition -->
    <div id="emotion" class="emotion"></div>

    <!-- Credit score -->
    <div id="score" class="score"></div>

</div>
  <div style="margin-left: 270px;"><EmotionAnalysis :DataDip="Datavoice" :resultdata="resultdata"></EmotionAnalysis>
</div>
</div>
</template>
<script>
import * as echarts from 'echarts'
import EmotionAnalysis from '@/components/EmotionAnalysis.vue'
export default {
  components: {
    EmotionAnalysis
  },
  data () {
    return {
      Datavoice: '声音情绪',
      audio: null,
      resultdata: [
        {
          emotion: 'Neutral',
          credit_score: 750
        },
        {
          emotion: 'Happy',
          credit_score: 850
        },
        {
          emotion: 'Neutral',
          credit_score: 750
        },
        {
          emotion: 'sad',
          credit_score: 850
        },
        {
          emotion: 'Fearful',
          credit_score: 150
        }
      ],
      number: 0,
      statussound: '',
      statusrecording: '',
      dataList: []
    }
  },
  methods: {
    // 声音播放
    startSound () {
      console.log('playAudio')
      if (this.statusrecording !== '') {
        return false
      }
      this.number = this.number + 1
      this.statussound = '(第' + this.number + '次播放中)'
      this.playAudio()
    },
    // 音频播放
    playAudio () {
      this.audio = new Audio('播放音频地址')
      this.audio.play()
      this.audio.onended = () => {
        this.statussound = ''
        console.log('playAudio')
      }
    },
    // 开始录音并识别
    startRecording () {
      if (this.number === 0 || this.statussound !== '') {
        return false
      }
      this.statusrecording = '(第' + this.number + '次录音中)'
      console.log('startRecording')
      this.$http.post('http://localhost:8090/sounddata.json', {
        voice_url: 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'
      }).then(res => {
        this.data = res.json()
        this.statusrecording = ''
        this.resultdata.push(this.data)
        // document.getElementById('result').innerText = `情绪: ${this.data.emotion}, 信用积分: ${this.data.credit_score}`
      }).$else(err => {
        console.log('请求错误')
        console.log(err)
      })
    },
    // 响应json数据转换
    getData () {
      this.resultdata.forEach(function (item) {
        this.dataList.push({
          value: item.credit_score,
          name: item.emotion
        })
      })
      console.log(this.dataList)
    }
  },
  // beforeRouteEnter: (to, from, next) => {
  //   next(vm => {
  //     vm.getData()
  //   })
  // },
  mounted () {
    // Waveform visualization (mock data)
    const waveformChart = echarts.init(document.getElementById('waveform'))
    const waveformOption = {
      title: {
        text: '音轨波形',
        left: 'center',
        textStyle: { color: '#ffffff' }
      },
      grid: {
        top: 10,
        bottom: 0

      },
      tooltip: {},
      xAxis: {
        type: 'category',
        show: false
      },
      yAxis: {
        type: 'value',
        show: false
      },
      series: [{
        name: 'Waveform',
        type: 'line',
        data: [0.5, 0.7, 0.8, 0.6, 0.3, 0.1, 0.5, 0.6, 0.4, 0.7, 0.9, 0.5, 0.3, 0.2],
        lineStyle: {
          color: '#00FFFF',
          width: 3
        }
      }]
    }
    waveformChart.setOption(waveformOption)

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
          data: [
            { value: 400, name: 'Angry' },
            { value: 850, name: 'Happy' },
            { value: 750, name: 'Neutral' },
            { value: 700, name: 'Sad' },
            { value: 599, name: 'Fearful' }
          ],
          // 替换成this.dataList会数据丢失
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          },
          itemStyle: {
            color: function (params) {
              const colorList = ['#FF4500', '#FFD700', '#32CD32', '#1E90FF', '#9400D3']
              return colorList[params.dataIndex]
            }
          }
        }
      ]
    }
    emotionChart.setOption(emotionOption)

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
        data: ['Angry', 'Happy', 'Neutral', 'Sad', 'Fearful'],
        axisLine: { lineStyle: { color: '#ffffff' } },
        axisLabel: { color: '#ffffff', fontSize: 11 }

      },
      yAxis: {
        type: 'value',
        axisLine: { lineStyle: { color: '#ffffff' } },
        axisLabel: { color: '#ffffff' }
      },
      grid: {
        top: '13%',
        bottom: '10%',
        left: '5%',
        right: '6%'
      },
      series: [{
        data: [400, 850, 750, 700, 599, 820],
        type: 'bar',
        itemStyle: {
          color: function (params) {
            const scoreColor = ['#FF4500', '#FFD700', '#32CD32', '#1E90FF', '#9400D3']
            return scoreColor[params.dataIndex]
          }
        }
      }]
    }
    scoreChart.setOption(scoreOption)
  }
}
</script>

<style scoped>
.voice-emotion{
    font-family: Arial, sans-serif;
    background-color: rgb(32, 46, 77);
    color: #ffffff;
    text-align: center;
}
.container {
    display: flex;
    justify-content: space-around;
    margin: 20px;
}
.waveform, .emotion, .score {
    width: 27%;
    height: 250px;
    padding: 20px;
    background-color: rgba(43, 62, 80, 0.9);
    border-radius: 10px;
    box-shadow: 0px 0px 20px rgba(0, 255, 255, 0.5);
}
h2 {
    margin-bottom: 20px;
}

</style>
