<template>
<div class="index">
    <sideBar></sideBar>
    <div class="body-right">
      <Header></Header>
      <div class="outer">
        <div class="func-top">
          <button @click="$router.go(-1)" style="color: #ffffff; width: 60px; height: 25px;background-color: transparent; outline: none; border: none;">
            <span
            style="padding-right: 10px; height: 25px; width: 50px; border-right: 3px solid #ffffff;"
            >
              &lt;&nbsp;返回</span>
          </button>

          <img src="../../assets/images/logo3.png" alt="">
          <img src="../../assets/images/logo2.png" alt="">
        </div>
        <div class="router-display"><router-view></router-view></div>
      </div>

      </div>
    </div>

</template>

<script>
import sideBar from '@/components/sideBar.vue'
import Header from '@/components/Header.vue'
export default {
  name: 'viewIndex',
  components: {
    sideBar,
    Header
  }

}
</script>

<style lang="less" scoped>

.index{
  background-color:#17223A;
  display: flex;
  flex-direction: row;
  height: 100%;
  width: 100%;
  color: aliceblue;
  // background-color: #17223A;
  .body-right{
    height: 100%;
    width: 90%;
    display: flex;
    flex-direction: column;
    align-items: center;
    // background-color: #2C3D50;
  }
  .outer{
    padding: 10px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    height: 85%;
    width: 98%;
    border-radius: 20px;
    margin: 0 auto;
    background-color: #202E4D;
    .func-top{
      padding: 5px;
      box-sizing: border-box;
      height: 40px;
      width: 100%;
      display: flex;
      flex-direction: row;
      align-items: center;
      border-radius:20px 20px 0px 0px;
      background-color: #202E4D;
      img:nth-of-type(1){
        margin-left: 20px;
        width: 50px;

      }
      img:nth-of-type(2){
        height: 30px;
        width: 160px;
      }
    }
    .router-display{
      box-sizing: border-box;
      height:610px;
      width: 100%;
      border-radius: 20px 20px 20px 20px;
      // background-color: #4c618f
    }
  }

}
</style>
