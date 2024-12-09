<template>
  <div class="outer">
    <div class="boxLine-1"></div>
      <button class="btn"></button><span>&nbsp;CPU</span>
  </div>

</template>
<script>
import * as echarts from 'echarts'
export default {
  mounted () {
    const myChart = echarts.init(document.querySelector('.boxLine-1'))
    const option = {
      title: {
        text: '一周消耗空间',
        textStyle: {
          color: '#ffffff'
        },
        left: 'center'
      },
      grid: {
        top: 40,
        bottom: 20,
        left: 80,
        right: 80
      },
      xAxis: {
        type: 'category',
        data: ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun'],
        axisLine: {
          show: false
        },
        splitLine: {
          show: true,
          lineStyle: {
            color: '#4F4F4F'
          }
        },
        axisLabel: {
          textStyle: {
            color: '#ffffff'
          }
        }
      },
      yAxis: {
        name: 'weekly consumption',
        nameTextStyle: {
          color: '#ffffff'
        },
        type: 'value',
        min: -100,
        max: 100,
        interval: 40,
        splitLine: {
          show: true,
          lineStyle: {
            color: '#4F4F4F'
          }
        },
        axisLabel: {
          textStyle: {
            color: '#ffffff'
          }
        }
      },
      series: [
        {
          data: [-60, -20, -60, 60, 0, 20],
          type: 'line'
        }
      ]
    }
    myChart.setOption(option)
  }
}
</script>

<style scoped>
.boxLine-1{
  width: 100%;
  height: 220px;
  margin-top: 20px;
  /* padding: 20px; */
  /* background-color: #293A50; */
  color: #ffffff;
}
.outer{
  position: relative;
}
.btn{
  margin-top: 30px;
  left: 100px;
  height: 15px;
  width:45px;
  font-size: 15px;
  background-color:#5470C6;
  outline: none;
  border: none;
  position: absolute;
}
span{
  font-size: 15px;
  margin-top: 30px;
  position: absolute;
  left: 160px;
}
</style>
