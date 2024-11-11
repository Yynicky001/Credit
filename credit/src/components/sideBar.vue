<template>
  <div class="side-bar">
      <div class="logo">
        <img src="../assets/images/logo.png" alt="">
      </div>
      <div class="list">
        <router-link class="sideli" to="/DashBoard"><img src="../assets//fonts//仪表盘.png" alt="">&nbsp;仪表盘</router-link>
        <router-link class="sideli" to="/UniInformation"><img src="../assets//fonts//统计信息.png" alt="">&nbsp;统计信息</router-link>
        <router-link class="sideli" to="/AuthLogin"><img src="../assets//fonts//身份认证.png" alt="">&nbsp;身份信息</router-link>
        <router-link class="sideli" to="/CreditHistory"><img src="../assets//fonts//历史积分.png" alt="">&nbsp;历史信贷积分</router-link>
        <router-link class="sideli" to="/FaceEmotion"><img src="../assets//fonts//Faceid.png" alt="">&nbsp;面部情绪识别</router-link>
        <router-link class="sideli" to="/VoiceEmotion"><img src="../assets//fonts//声音识别.png" alt="">&nbsp;声音情绪识别</router-link>
        <router-link class="sideli" to="/creditScore"><img src="../assets//fonts//huitu-atlas.png" alt="">&nbsp;综合信贷积分</router-link>
        <router-link class="sideli" to="/AboutPro"><img src="../assets//fonts//关于.png" alt="">&nbsp;关于项目</router-link>
      </div>
      <div class="setting"><img src="../assets/fonts/设置.png" alt="">设置</div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>

.side-bar{
  margin: 20px 0;
  height: 720px;
  width: 280px;
  border-right:rgba(128, 128, 128, 0.53) 3px solid;
  display: flex;
  flex-direction: column;
}
.logo{
  height: 160px;
  width: 280px;
  img{
    height: 100%;
    width: 100%;
  }
}
.list{
  display: flex;
  flex-direction: column;
  height: 540px;
  width: 280px;
  .sideli{
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 10px 0;
    margin-left: 30px;
    line-height: 36px;
    border-radius: 10px;
    height: 36px;
    width: 75%;
    text-align: center;
    font-size: 22px;
    font-weight: 400;
    background-color: #ffffff;
    color: black;
    text-decoration: none;
    .router-link-active{
      background-color: rgba(219, 245, 255, 0.684);
    }
    img{
      height: 22px;
      width: 22px;
      // background-color: #ffffff;
    }
  }
  .router-link-active{
      background-color: #ABD0EC;
    }
}
.setting{
  padding-left: 35px;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  height: 150px;
  width: 280px;
  color: #ffffff;
  font-size: 20px;
  font-weight: 300;
  // background-color: aquamarine;
  img{
    height: 22px;
    width: 22px;
    color: white;
  }
}

</style>
