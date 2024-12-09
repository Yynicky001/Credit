<template>
  <div class="operation-tip-container">
    <p class="operation-tip">{{ message }}</p>
  </div>
</template>
<script>
export default {
  name: 'MessagePopup',
  props: {
    message: {
      type: String,
      default: ''
    }
  }
}
</script>
<style scoped>
.operation-tip-container {
  height: 20px;
  margin-bottom: 20px;
  padding: 1px;
  background:radial-gradient(circle at center, #5562c77d, #202e4d21);;
  box-shadow: 0 1px 0px rgb(112, 245, 250) inset, 0 -1px 0 rgb(112, 250, 234) inset;
  border: 0px;
  text-align: center;
  color: #eb6d6d;
}
.operation-tip {
  font-size: 14px;
}
</style>
