<template>
  <div class="credit-score scrollable-list-container">
    <ul type="none" class="score-item" v-for="item in resultdata" :key="item.id">
      <li class="emotion-item">{{ DataDip }}</li>
      <li>{{item.emotion}}</li>
      <li class="emotion-item">情绪对应积分</li>
      <li class="score">{{item.credit_score}}</li>
    </ul>
  </div>
</template>
<script src="emotionService.js"></script>
<script>
export default {
  // 父组件数据接收
  props:{
    DataDip: {
      type: String,
      default: 'DataDip'
    },
    resultdata: {
      type: Array,
      default: () => []
    }
  },
  name: 'EmotionAnalysis',
  // data () {
  //   return {
  //     emotionList: []
  //   }
  // },
  // beforeRouteEnter: (to,from,next) => {
  //   next(vm => {

  //   });
  // },
  // methods: {
  //   getData: function (resData) {
  //     this.$http.post('http://8090/data.json', {
  //     }).then(res => {
  //       this.emotionList.append(res.json())
  //     }).$else(err => {
  //       console.log('请求错误')
  //       console.log(err)
  //     })
  //   }
  // },
}
</script>

<style scoped lang="less">
.scrollable-list-container {
  max-height: 190px; /* 设置容器的最大高度*/
  overflow-y: auto; /* 出现垂直滚动条 */
  scrollbar-width: none;
  -ms-overflow-style: none;
}
.score-item{
  display: flex;
  flex-direction: row;
  line-height: 30px;
  li{
    width: 120px;
    text-align: center;
    padding: 5px 20px;
    border-radius: 2px;
    margin: 2px 0;
    background-color: rgba(181, 246, 232, 0.041);
  }
  .emotion-item{

    background-color: rgba(181, 246, 232, 0.070);
  }
}
</style>
