<template>
    <canvas ref="audioCanvas"></canvas>
</template>
<script>
export default {
  name: 'AudioVisualizer',
  props: {
    config: {
      type: Object,
      default: () => ({
        canvasWidth: window.innerWidth * 0.9,
        canvasHeight: 400,
        barWidth: 10,
        barSpacing: 2,
        barHeightScale: 200
      })
    }
  },
  mounted () {
    this.initializeAudioVisualizer(this.$refs.audioCanvas)
  },
  methods: {
    initializeAudioVisualizer (canvas) {
      if (!canvas) {
        console.error('Canvas element not found')
        return
      }
      const ctx = canvas.getContext('2d')
      if (!ctx) {
        console.error('Failed to get 2D context')
        return
      }
      const { canvasWidth, canvasHeight, barWidth, barSpacing, barHeightScale } = this.config
      canvas.width = canvasWidth
      canvas.height = canvasHeight
      const numBars = Math.floor(canvasWidth / barWidth)
      const dataArray = new Uint8Array(numBars)
      const targetDataArray = new Uint8Array(numBars)
      const generateTargetAudioData = () => {
        for (let i = 0; i < numBars; i++) {
          targetDataArray[i] = Math.random() * 255
        }
      }
      const smoothData = () => {
        for (let i = 0; i < numBars; i++) {
          dataArray[i] += (targetDataArray[i] - dataArray[i]) * 0.1
        }
      }
      const drawBars = () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height)
        for (let i = 0; i < numBars; i++) {
          const barHeight = (dataArray[i] / 255) * barHeightScale
          const gradient = ctx.createLinearGradient(0, 0, 0, canvas.height)
          gradient.addColorStop(0, '#00eaff')
          gradient.addColorStop(1, '#00ff6a')
          ctx.fillStyle = gradient
          const x = i * (barWidth + barSpacing)
          const y = canvasHeight / 2
          ctx.fillRect(x, y - barHeight, barWidth, barHeight)
          ctx.fillRect(x, y, barWidth, barHeight)
        }
      }
      const update = () => {
        smoothData()
        drawBars()
        requestAnimationFrame(update)
      }
      generateTargetAudioData()
      setInterval(generateTargetAudioData, 1000)
      update()
    }
  }
}
</script>
  <style scoped>
  canvas {
    display: block;
    background-color: #324a5f;
    border: 1px solid #324a5f;
  }
</style>
