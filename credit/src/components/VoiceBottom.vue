<!-- <template>
    <div>
      <button @onclick="startSound()" style="margin-right:20px;width: 100px;height: 25px;border-radius: 20px;">播放声音</button>
      <button @onclick="startRecording()" style="width: 150px;height: 25px;border-radius: 20px;">开始录音并识别情绪</button>
    </div>
</template>

<script>
export default {
  name: 'VoiceBottom',
  data () {
    return {
      audio: null,
      popupVisible: false,
      data: [],
      numer: 0
    }
  },
  methods: {
    showPopup () {
      this.popupVisible = true
      this.playAudio()
    },
    playAudio () {
      this.audio = new Audio('文件')
      this.number = this.number + 1
      this.audio.play()
      this.audio.onended = () => {
        this.popupVisible = false
      }
    },
    startRecording () {
      this.$http.post('http://127.0.0.1:5000/predict_emotion', {
        voice_url: 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'
      }).then(res => {
        this.data = res.json()
        document.getElementById('result').innerText = `情绪: ${this.data.emotion}, 信用积分: ${this.data.credit_score}`
      })
    }
  }
}
</script> -->
