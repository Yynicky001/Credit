<template>
  <div class="uni-information">
    <h2>统计信息</h2>
    <div class="container">
        <div id="line-chart" class="chart-container">
            <div class="legend">
                <p>绿色: 高兴 (happy)</p>
                <p>橙色: 悲伤 (sad)</p>
            </div>
        </div>
        <div id="bar-chart" class="chart-container">
            <div class="legend">
                <p>颜色说明: 各种情绪分布</p>
            </div>
        </div>
        <div id="pie-chart" class="chart-container">
            <div class="legend">
                <p>颜色说明: 声音情绪分布</p>
            </div>
        </div>
        <div id="radar-chart" class="chart-container">
            <div class="legend">
                <p>颜色说明: 信用积分趋势</p>
            </div>
        </div>
    </div>

  </div>
</template>

<script>
import * as echarts from 'echarts'
export default {
  mounted () {
    // 图表1：面部情绪随时间变化（折线图）
    const lineChart = echarts.init(document.getElementById('line-chart'))
    const lineOption = {
      grid: {
        top: 50,
        bottom: 25
      },
      title: {
        text: '面部情绪随时间变化图',
        left: 'center',
        textStyle: { color: '#ffffff' }
      },
      tooltip: { trigger: 'axis' },
      xAxis: {
        type: 'category',
        data: ['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00'],
        axisLabel: { color: '#ffffff' },
        axisLine: { lineStyle: { color: '#ffffff' } }
      },
      yAxis: {
        type: 'value',
        name: '情绪指数',
        nameTextStyle: { color: '#ffffff' },
        axisLabel: { color: '#ffffff' },
        axisLine: { lineStyle: { color: '#ffffff' } }
      },
      series: [
        {
          name: '高兴 (happy)',
          type: 'line',
          data: [10, 20, 15, 30, 25, 35, 40],
          lineStyle: {
            color: '#00FF00',
            width: 3,
            shadowColor: 'rgba(0, 255, 0, 0.5)',
            shadowBlur: 10
          }
        },
        {
          name: '悲伤 (sad)',
          type: 'line',
          data: [5, 15, 20, 10, 20, 25, 15],
          lineStyle: {
            color: '#FF4500',
            width: 3,
            shadowColor: 'rgba(255, 69, 0, 0.5)',
            shadowBlur: 10
          }
        }
      ]
    }
    lineChart.setOption(lineOption)

    // 图表2：情绪状态统计（柱状图）
    const barChart = echarts.init(document.getElementById('bar-chart'))
    const barOption = {
      title: {
        text: '情绪状态分布图',
        left: 'center',
        textStyle: { color: '#ffffff' }
      },
      grid: {
        top: 50,
        bottom: 25

      },
      tooltip: { trigger: 'axis' },
      xAxis: {
        type: 'category',
        data: ['高兴', '悲伤', '愤怒 ', '惊讶', '厌恶', '恐惧', '中立'],
        axisLabel: { color: '#ffffff' },
        axisLine: { lineStyle: { color: '#ffffff' } }
      },
      yAxis: {
        type: 'value',
        name: '次数',
        nameTextStyle: { color: '#ffffff' },
        axisLabel: { color: '#ffffff' },
        axisLine: { lineStyle: { color: '#ffffff' } }
      },
      series: [
        {
          name: '情绪状态',
          type: 'bar',
          data: [30, 15, 10, 12, 8, 7, 18],
          itemStyle: {
            color: '#3398DB',
            shadowColor: 'rgba(0, 136, 212, 0.5)',
            shadowBlur: 10
          }
        }
      ]
    }
    barChart.setOption(barOption)

    // 图表3：声音情绪分布（饼图）
    const pieChart = echarts.init(document.getElementById('pie-chart'))
    const pieOption = {
      title: {
        text: '声音情绪分布图',
        left: 'center',
        textStyle: { color: '#ffffff' }
      },
      tooltip: {
        trigger: 'item',
        formatter: '{b}: {c} ({d}%)'
      },
      series: [
        {
          name: '声音情绪',
          type: 'pie',
          radius: '66%',
          center: ['50%', '55%'],
          data: [
            { value: 20, name: '高兴 (happy)' },
            { value: 15, name: '悲伤 (sad)' },
            { value: 10, name: '愤怒 (angry)' },
            { value: 5, name: '惊讶 (surprised)' },
            { value: 3, name: '厌恶 (disgusted)' },
            { value: 2, name: '恐惧 (fearful)' },
            { value: 5, name: '中立 (neutral)' }
          ],
          itemStyle: {
            borderColor: '#ffffff',
            borderWidth: 2,
            shadowColor: 'rgba(0, 0, 0, 0.5)',
            shadowBlur: 20
          },
          label: {
            color: '#ffffff'
          }
        }
      ]
    }
    pieChart.setOption(pieOption)

    // 图表4：历史征信积分（雷达图）
    const radarChart = echarts.init(document.getElementById('radar-chart'))
    const radarOption = {
      title: {
        text: '历史征信积分对比',
        left: 'center',
        textStyle: { color: '#ffffff' }

      },
      tooltip: {},
      radar: {
        center: ['50%', '60%'],
        indicator: [
          { name: '2023 Q1', max: 1000 },
          { name: '2023 Q2', max: 1000 },
          { name: '2023 Q3', max: 1000 },
          { name: '2023 Q4', max: 1000 },
          { name: '2024 Q1', max: 1000 }
        ],
        splitLine: {
          lineStyle: { color: '#ffffff' }
        },
        splitArea: {
          areaStyle: { color: 'rgba(0, 136, 212, 0.1)' }
        }
      },
      series: [
        {
          name: '信用积分',
          type: 'radar',
          data: [
            {
              value: [730, 680, 720, 740, 780],
              name: '2023年'
            },
            {
              value: [800, 750, 820, 860, 880],
              name: '2024年'
            }
          ],
          itemStyle: {
            color: 'rgba(0, 255, 255, 0.7)',
            borderColor: '#ffffff',
            borderWidth: 2,
            shadowColor: 'rgba(0, 255, 255, 0.5)',
            shadowBlur: 15
          },
          lineStyle: {
            color: '#00FFFF',
            width: 3
          }
        }
      ]
    }
    radarChart.setOption(radarOption)
  }
}
</script>

<style scoped>
.uni-information{
  height: 100%;
  width: 100%;
    background-color: rgb(32, 46, 77);
    color: #ffffff;
    font-family: Arial, sans-serif;
}
.container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    align-items: center;
    margin: 0px;
}
.chart-container {
    width: 45%;
    height: 245px;
    margin: 14px;
    border: 2px solid #2b3e50;
    border-radius: 15px;
    box-shadow: 0px 0px 20px rgba(0, 255, 255, 0.5);
    background: rgba(43, 62, 80, 0.8);
    position: relative;
}
.legend {
    position: absolute;
    top: 10px;
    left: 10px;
    color: #ffffff;
    font-size: 14px;
    background: rgba(0, 0, 0, 0.5);
    padding: 5px;
    border-radius: 5px;
}
h2 {
    text-align: center;
    margin: 0px 0;
}
</style>
