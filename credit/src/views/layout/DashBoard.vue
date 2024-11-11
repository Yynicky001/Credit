<template>
  <div class="Dashboard">
    <h2>资源占用率仪表盘</h2>

<div class="container">
    <div id="cpuGauge" class="gauge"></div>
    <div id="memoryGauge" class="gauge"></div>
    <div id="diskGauge" class="gauge"></div>
    <div id="networkGauge" class="gauge"></div>
</div>
<ChartDisplay></ChartDisplay>
  </div>

</template>

<script>
import * as echarts from 'echarts'
import ChartDisplay from '@/components/ChartDisplay.vue'
export default {
  name: 'DashBoard',
  components: {
    ChartDisplay
  },
  mounted () {
    function createGaugeChart (id, title, value) {
      const gaugeChart = echarts.init(document.getElementById(id))
      const gaugeOption = {
        title: {
          text: title,
          left: 'center',
          textStyle: { color: '#ffffff' }, // Title color set to white
          top: '10%'
        },
        tooltip: {
          formatter: '{a} <br/>{b} : {c}%'
        },
        series: [
          {
            center: ['50%', '60%'],
            name: title,
            type: 'gauge',
            detail: {
              formatter: '{value}%',
              color: '#ffffff', // Detail color set to white
              fontSize: 18

            },
            data: [{ value: value }],
            axisLine: {
              lineStyle: {
                color: [[0.3, '#00FF00'], [0.7, '#FFD700'], [1, '#FF4500']],
                width: 10
              }
            },
            axisLabel: {
              color: '#ffffff', // Label color set to white
              distance: 12
            },
            splitLine: {
              show: true,
              length: 10,
              lineStyle: {
                color: '#ffffff',
                width: 2
              }
            },
            axisTick: {
              length: 5
            },
            title: {
              fontSize: 14,
              color: '#ffffff' // Title font color set to white
            }
          }
        ]
      }
      gaugeChart.setOption(gaugeOption)
    }

    // Creating gauge charts for different resources
    createGaugeChart('cpuGauge', 'CPU占用率', 65) // Example CPU usage
    createGaugeChart('memoryGauge', '内存占用率', 45) // Example Memory usage
    createGaugeChart('diskGauge', '磁盘占用率', 70) // Example Disk usage
    createGaugeChart('networkGauge', '网络占用率', 30) // Example Network usage
  }
}
</script>

<style scoped>
.Dashboard{
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
.gauge {
    width: 30%;
    height: 240px;
    background-color:  rgb(32, 46, 77);
    border-radius: 10px;
    box-shadow: 0px 0px 20px rgba(0, 255, 255, 0.5);
}
h2 {
    margin-bottom: 20px;
}
</style>
