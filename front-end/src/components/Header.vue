<template>
  <div class="Hearder">
   主页&nbsp;/
    <div class="login-box">您好，{{username}}，欢迎使用
     <button @click="$router.push('/UserLogin')">登陆</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HeaderIndex',
  data () {
    return {
      username: ''
    }
  },
  methods: {
    async getUserInfo () {
      axios.get('http://127.0.0.1:5000/get_user_info')
        .then(res => {
          this.username = res.data.username
          console.log(res.data.username)
        })
    }
  },
  mounted () {
    // this.getUserInfo()
  }
}
</script>

<style lang="less" scoped>
.Hearder{
  height: 70px;
  width: 100%;
  line-height: 70px;
  padding:0 20px;
  box-sizing: border-box;
  color: white;
  display: flex;
  flex-direction: row;
  .main-page{
    width: 50px;
    height: 70px;
    line-height: 70px;
  }
  // background-color: aliceblue;
  .login-box{
    width: 400px;
    margin-left: 730px;
    display: flex;
    flex-direction: row;
    align-items: center;
    button{
      margin-left: 30px;
      height: 30px;
      width: 100px;
      border-radius: 5px;
      border: none;
      color: white;
      background-color: #34CEFF;
    }
  }
}
</style>
