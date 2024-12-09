<template>
  <div class="credit-history">
    <h2>历史信贷积分</h2>
    <div class="container">
        <div id="scatter-chart" class="chart-container"></div>
        <div id="stacked-bar-chart" class="chart-container"></div>
    </div>
    <CreditScoreItem :resData="resData"></CreditScoreItem>
  </div>
</template>
<script>
import * as echarts from 'echarts'
import CreditScoreItem from '@/components/CreditScoreItem.vue'
import { mapState } from 'vuex'
// import { eventBus } from '../../services/eventBus'

export default {
  data () {
    return {
      resData: [
        {
          option: '操作1',
          name: '张三',
          username: 'zhangsan',
          sex: '男',
          credit_score: 80,
          remark: '备注1'
        },
        {
          option: '操作2',
          name: '李四',
          username: 'lisi',
          sex: '女',
          credit_score: 90,
          remark: '备注2'
        },
        {
          option: '操作2',
          name: '李四',
          username: 'lisi',
          sex: '女',
          credit_score: 90,
          remark: '备注2'
        },
        {
          option: '操作2',
          name: '李四',
          username: 'lisi',
          sex: '女',
          credit_score: 90,
          remark: '备注2'
        }
      ]
    }
  },
  components: {
    CreditScoreItem
  },
  mounted () {
    const scatterChart = echarts.init(document.getElementById('scatter-chart'))
    const scatterOption = {
      title: {
        text: '信贷评分与负债收入比关系',
        left: 'center',
        textStyle: { color: '#ffffff' }
      },
      tooltip: {
        trigger: 'axis',
        // showDelay: 0,
        // formatter: function (params) {
        //   return '信贷评分: ' + params.value[1] + '<br/>负债比: ' + params.value[1] + '%'
        // },
        axisPointer: {
          show: true,
          type: 'cross',
          lineStyle: {
            type: 'dashed',
            color: '#ffffff'
          }
        }
      },
      grid: {
        left: '10%',
        right: '10%',
        bottom: '10%'
      },
      xAxis: {
        type: 'value',
        name: '收入',
        nameTextStyle: { color: '#ffffff' },
        axisLabel: { color: '#ffffff' },
        axisLine: { lineStyle: { color: '#ffffff' } }
      },
      yAxis: {
        type: 'value',
        name: '负债比 (%)',
        nameTextStyle: { color: '#ffffff' },
        axisLabel: { color: '#ffffff' },
        axisLine: { lineStyle: { color: '#ffffff' } }
      },
      series: [
        {
          name: '信贷评分',
          type: 'scatter',
          data: [
            [5000, 20, 750],
            [8000, 35, 850],
            [10000, 40, 620],
            [6000, 25, 720],
            [9500, 18, 790]
          ],
          symbolSize: function (data) {
            return data[2] / 20 // size based on credit score
          },
          itemStyle: {
            color: function (params) {
              if (params.value[2] > 800) return '#00FF00'
              else if (params.value[2] > 700) return '#FFCC00'
              else return '#FF4500'
            }
          }
        }
      ]
    }
    scatterChart.setOption(scatterOption)

    // Stacked Bar Chart: 各信贷指标贡献
    const stackedBarChart = echarts.init(document.getElementById('stacked-bar-chart'))
    const stackedBarOption = {
      title: {
        text: '信贷评分各指标贡献',
        left: 'center',
        textStyle: { color: '#ffffff' }
      },
      tooltip: {
        trigger: 'axis',
        axisPointer: { type: 'shadow' }
      },
      legend: {
        top: '6%',
        data: ['信贷历史', '逾期次数', '信用卡使用率', '负债收入比', '资产负债情况', '收入稳定性', '信用账户数量'],
        textStyle: { color: '#ffffff' }
      },
      grid: {
        top: '30%',
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
      },
      xAxis: {
        type: 'category',
        data: ['用户1', '用户2', '用户3', '用户4', '用户5'],
        axisLabel: { color: '#ffffff' },
        axisLine: { lineStyle: { color: '#ffffff' } }
      },
      yAxis: {
        type: 'value',
        name: '得分',
        nameTextStyle: { color: '#ffffff' },
        axisLabel: { color: '#ffffff' },
        axisLine: { lineStyle: { color: '#ffffff' } }
      },
      series: [
        {
          name: '信贷历史',
          type: 'bar',
          stack: '总分',
          data: [100, 150, 120, 130, 140],
          itemStyle: { color: '#1f77b4' }
        },
        {
          name: '逾期次数',
          type: 'bar',
          stack: '总分',
          data: [50, 50, 100, 50, 50],
          itemStyle: { color: '#ff7f0e' }
        },
        {
          name: '信用卡使用率',
          type: 'bar',
          stack: '总分',
          data: [120, 100, 130, 110, 120],
          itemStyle: { color: '#2ca02c' }
        },
        {
          name: '负债收入比',
          type: 'bar',
          stack: '总分',
          data: [150, 100, 150, 130, 150],
          itemStyle: { color: '#d62728' }
        },
        {
          name: '资产负债情况',
          type: 'bar',
          stack: '总分',
          data: [100, 100, 100, 120, 130],
          itemStyle: { color: '#9467bd' }
        },
        {
          name: '收入稳定性',
          type: 'bar',
          stack: '总分',
          data: [50, 100, 100, 80, 50],
          itemStyle: { color: '#8c564b' }
        },
        {
          name: '信用账户数量',
          type: 'bar',
          stack: '总分',
          data: [150, 150, 120, 160, 150],
          itemStyle: { color: '#e377c2' }
        }
      ]
    }
    stackedBarChart.setOption(stackedBarOption)
  },
  computed: {
    ...mapState(['sharedResData'])
  }
  // created () {
  //   eventBus.$on('sendresData', (resData) => {
  //     this.resData = resData
  //   })
  // }
  // methods: {
  //   sendresData () {
  //     console.log(this.sharedResData)
  //   }
  // }
}
</script>

<style scoped>
.credit-history{
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
    height: 300px;
    margin: 20px;
    border: 2px solid #2b3e50;
    border-radius: 15px;
    box-shadow: 0px 0px 20px rgba(0, 255, 255, 0.5);
    background: rgba(43, 62, 80, 0.8);
}
h2 {
    text-align: center;
    margin: 10px 0;
}
</style>
