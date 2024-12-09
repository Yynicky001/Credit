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
  name: 'EmotionAnalysis',
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
}
</script>

<style scoped lang="less">
.scrollable-list-container {
  max-height: 240px; /* 设置容器的最大高度*/
  overflow-y: auto; /* 出现垂直滚动条 */
  scrollbar-width: none;
  padding: 0px 10px;
  -ms-overflow-style: none;
  border-radius: 5px;
  box-shadow: 0px 0px 20px rgba(0, 255, 255, 0.5);
  background-color: rgba(43, 62, 80, 0.9);
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
