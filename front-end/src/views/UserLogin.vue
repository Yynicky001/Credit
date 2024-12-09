<template>
  <div class="user-login">
    <div class="img-box">
      <img src=".././assets/images/logo01.png" alt="">
    </div>
    <div class="content-box">
      <h4>登录界面</h4>
      <span class="content-text">用户名：</span><br>
      <input type="text" name="" id="" placeholder="请输入用户名"><br>
      <span class="content-text" style="margin-top: 40px;">密码：</span><br>
      <input  type="password" placeholder="请输入密码">
      <button class="login-btn">登录</button>
      <button class="forget-btn">忘记密码？</button>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.user-login {
  width: 32%;
  height: 98%;
  margin: 0 auto;
  background-color: #e3eff1;
  border-radius: 20px;
  .img-box{
    img{
      width: 100%;
      height: 100%;
      text-align: center;
    }
    margin: 0 auto;
    height: 28%;
    width:90%;
  }
  .content-box{
    // font-weight: 500;
    line-height: 35px;
    color:rgb(13, 30, 94);
    // background-color: antiquewhite;
    h4{
      text-align: center;
    }
    .content-text{
      margin-left:40px;

    }
    input{
      padding-left: 6px;
      margin-left: 40px;
      margin-bottom: 20px;
      width: 80%;
      height: 30px;
      border: 1px solid rgb(43, 114, 142);
      border-radius: 5px;
    }
    input:focus{
      outline: none;
      border: 3px solid rgba(43, 114, 142, 0.223);
    }
    .login-btn{
      border: none;
      margin-left: 40px;
      width: 80%;
      height: 30px;
      color: white;
      border-radius: 5px;
      background-color: #2980B9;
    }
    .forget-btn{
      border: none;
      margin-left: 44px;
      width: 80%;
      height: 30px;
      color: #2980B9;
      border-radius: 5px;
      background-color: #297fb900;
    }
  }
}

</style>
