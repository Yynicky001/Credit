<template>
  <div class="face-emotion" >
        <!-- 环形图与柱状图布局 -->
    <div class="Piechart-box">
      <!-- 摄像头图像放置 -->
   <div class="camera">
    <button class="bt" @click="toggleCamera">点击打开摄像头</button>
   </div>
    <div id="pieChart" style="width: 55%; height: 160%;"></div>
    </div>
    <div class="Barchart-box" style="width: 100%; height: 70%;">
      <div id="barChart" style="width: 45%; height: 100%;" ></div>
    </div>
    <div class="feiqilai">
    <div class="form-container">
      <table>
        <thead>
          <tr>
            <th>情绪</th>
            <th>积分</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in emotionScores" :key="index">
            <td>{{ item.emotion }}</td>
            <td>{{ item.score }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  </div>
</template>

<script>
import * as echarts from 'echarts'
export default {
  components: {},
  data () {
    return {
      Dataface: '面部情绪',
      cameraStatus: false,
      emotionScores: [
        { emotion: 'angry', score: 400 },
        { emotion: 'surprised', score: 700 },
        { emotion: 'sad', score: 650 },
        { emotion: 'fearful', score: 550 },
        { emotion: 'happy', score: 850 },
        { emotion: 'neutral', score: 750 },
        { emotion: 'fearful', score: 550 },
        { emotion: 'happy', score: 850 },
        { emotion: 'surprised', score: 700 },
        { emotion: 'sad', score: 650 },
        { emotion: 'happy', score: 850 }
      ]
    }
  },
  methods: {
    // 切换摄像头状态
    toggleCamera () {
      let action// 如果摄像头是开着的，关闭它；反之亦然
      if (this.cameraStatus) {
        action = false
      } else {
        action = true
      }
      // 向后端发送请求来控制摄像头
      this.controlCamera(action)
    },

    // 控制摄像头开关的函数
    async controlCamera (runCamera) {
      try {
        const response = await fetch('http://localhost:5080/control_camera', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ run_camera: runCamera })
        })

        const result = await response.json()
        console.log(result)

        // 根据后端返回的状态更新前端显示的状态
        this.cameraStatus = runCamera
      } catch (error) {
        console.error('Error:', error)
        alert('请求失败，请检查后端服务是否运行')
      }
    }
  },
  mounted () {
    // 环形图实例
    const pieChart = echarts.init(document.getElementById('pieChart'))
    // 柱状图实例
    const barChart = echarts.init(document.getElementById('barChart'))

    // 环形图的初始配置
    const pieOption = {
      backgroundColor: 'rgb(32, 46, 77)', // 背景颜色保持不变
      title: {
        text: '面部情绪识别',
        left: 'center',
        top: 5,
        textStyle: {
          color: '#fff',
          fontSize: 20
        }
      },
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
      },
      legend: {
        orient: 'vertical',
        left: 10,
        textStyle: {
          color: '#fff'
        }
      },
      series: [
        {
          name: 'Emotion Probability',
          type: 'pie',
          center: ['50%', '57%'], // 控制环形图的位置
          radius: ['40%', '70%'], // 控制环形图的内外半径
          avoidLabelOverlap: false,
          label: {
            show: true,
            position: 'outside',
            textStyle: {
              fontSize: 14,
              color: '#fff'
            }
          },
          labelLine: {
            show: true,
            lineStyle: {
              color: '#fff'
            }
          },
          itemStyle: {
            borderRadius: 10,
            borderColor: '#000',
            borderWidth: 2,
            shadowBlur: 10,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          },
          color: [
            'rgb(225, 0, 0)', // Angry - 红色
            'rgb(208, 255, 1)', // Disgusted - 亮绿色
            'rgb(221, 1, 225)', // Fearful - 紫色
            'rgb(251, 255, 1)', // Happy - 明亮的黄色
            'rgb(1, 1, 225)', // Sad - 蓝色
            'rgb(0, 225, 225)', // Surprised - 青色
            'rgb(1, 255, 183)' // Neutral - 淡绿色
          ],
          data: [
            { value: 20, name: 'Angry' },
            { value: 15, name: 'Disgusted' },
            { value: 10, name: 'Fearful' },
            { value: 25, name: 'Happy' },
            { value: 30, name: 'Sad' },
            { value: 15, name: 'Surprised' },
            { value: 10, name: 'Neutral' }
          ]
        }
      ]
    }

    // 柱状图的初始配置
    const barOption = {
      backgroundColor: 'rgb(32, 46, 77)',
      title: {
        text: '综合情绪识别',
        left: 'center',
        top: 5,
        textStyle: {
          color: '#fff',
          fontSize: 20
        }
      },
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow'
        }
      },
      xAxis: {
        type: 'category',
        data: ['Angry', 'Disgusted', 'Fearful', 'Happy', 'Sad', 'Surprised', 'Neutral'],
        axisLine: {
          lineStyle: {
            color: '#fff'
          }
        },
        axisLabel: {
          fontSize: 10
        }
      },
      yAxis: {
        type: 'value',
        axisLine: {
          lineStyle: {
            color: '#fff'
          }
        },
        splitLine: {
          lineStyle: {
            type: 'dashed',
            color: '#555'
          }
        }
      },
      grid: {
        top: '15%',

        left: '3%',
        right: '4%',
        bottom: '0%',
        containLabel: true
      },
      series: [
        {
          name: 'Probability',
          type: 'bar',
          barWidth: '60%',
          itemStyle: {
            color: function (params) {
              // 为每个情绪类别分配不同的颜色
              const colors = ['rgb(225, 0, 0)', 'rgb(208, 255, 1)', 'rgb(221, 1, 225)', 'rgb(251, 255, 1)', 'rgb(1, 1, 225)', 'rgb(0, 225, 225)', 'rgb(1, 255, 183)']
              return colors[params.dataIndex]
            },
            shadowBlur: 10,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          },
          label: {
            show: true,
            position: 'top',
            color: '#fff',
            fontSize: 14
          },
          data: [20, 15, 10, 25, 30, 15, 10]
        }
      ]
    }

    // 初始化图表
    pieChart.setOption(pieOption)
    barChart.setOption(barOption)

    // 模拟情绪识别概率的动态变化（每1秒更新一次）
    setInterval(function () {
      // 随机生成新数据
      const newData = [
        { value: Math.round(Math.random() * 50), name: 'Angry' },
        { value: Math.round(Math.random() * 50), name: 'Disgusted' },
        { value: Math.round(Math.random() * 50), name: 'Fearful' },
        { value: Math.round(Math.random() * 50), name: 'Happy' },
        { value: Math.round(Math.random() * 50), name: 'Sad' },
        { value: Math.round(Math.random() * 50), name: 'Surprised' },
        { value: Math.round(Math.random() * 50), name: 'Neutral' }
      ]
      const barData = newData.map(item => item.value) // 将环形图的数据同步到柱状图

      // 更新环形图数据
      pieOption.series[0].data = newData
      pieChart.setOption(pieOption, true)

      // 更新柱状图数据
      barOption.series[0].data = barData
      barChart.setOption(barOption, true)
    }, 1000) // 每隔1秒更新一次数据
  }
}
</script>

<style>
.feiqilai {
  transform: scale(0.8);
  position: absolute;
  width: 600px;
  bottom: -40%;
  right: 0;
}
.Piechart-box{
  position: relative;
  height: 60%;
  width: 100%;
  display: flex;
  flex-direction: row;
}
.camera{
  height:250px;
  width: 500px;
  background-color: rgba(240, 248, 255, 0.305);
}
.face-emotion{
  position: relative;
  height: 440px;
  margin: 0;
  background-color: rgb(32, 46, 77);

}
.Barchart-box{
  height: 50%;
  width: 100%;
  display: flex;
  flex-direction: row;
}

#pieChart{
  position: absolute;
  overflow: visible;
  top: -40px;
  left: 500px;
}
.table-box{
  margin: 0 auto;
  height: 100%;
  width: 46%;
}
.analyse-box{
  margin-left: 10px;
  margin-top:130px ;
}
.form-container {
  max-height: 250px; /* 限制容器的最大高度 */
  overflow-y: auto; /* 启用纵向滚动条 */
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 4px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  font-weight: bold;
}

</style>
