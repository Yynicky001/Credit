<template>
<div class="score-item scrollable-list-container">
<table>
  <thead>
    <tr>
      <th>操作</th>
      <th>姓名</th>
      <th>用户名</th>
      <th>性别</th>
      <th>历史积分</th>
      <th>备注</th>
    </tr>
  </thead>
  <tbody >
    <tr v-for="item in resData" :key="item.id">
      <td>{{item.option}}</td>
      <td>{{item.name}}</td>
      <td>{{item.username}}</td>
      <td>{{item.sex}}</td>
      <td>{{item.credit_score}}</td>
      <td>{{item.remark}}</td>
    </tr>
  </tbody>
</table>
</div>
</template>

<script>
export default {
  props: {
    // 父组件数据接收
    resData: {
      type: Array,
      default: () => []
    }
  },
  methods: {
    consoleLog: function (resData) {
      console.log(resData)
    }
  }
}
</script>

<style lang="less" scoped>
.scrollable-list-container {
  max-height: 125px; /* 设置容器的最大高度 */
  overflow-y: auto; /* 出现垂直滚动条 */
  scrollbar-width: none;
  -ms-overflow-style: none;
}
.score-item{
  width: 100%;
  height: 40%;
  margin: 0px auto;
  table{
    border-radius:20px ;
    border-collapse: collapse;
    width: 100%;
    height: 100%;
    text-align: center;
    line-height: 35px;
    th{
      border: 3px rgba(0, 0, 0, 0.134) solid;
      background-color: rgba(177, 181, 186, 0.173);
    }
    td{
      border: 3px rgba(0, 0, 0, 0.134) solid;
      background-color: rgba(123, 128, 133, 0.173)
    }
  }
}
</style>
