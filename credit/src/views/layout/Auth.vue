<template>
  <div class=content>
    <span class="sign">*</span>用户名<br><input type="text" placeholder="请输入您的用户名" class="input1"
        id="usernameInput" v-model="formData.username"><br>
    <span class="sign">*</span>姓名<br><input type="text" placeholder="请输入您的姓名" class="input1"
        id="nameInput" v-model="formData.name"><br>

    <div class="sex">
        <!-- *头像<input type="text" value="请选择您的头像"> -->
        <span class="sign">*</span>性别<br>
        <select id="genderlist" v-model="formData.sex">
          <option value="请选择">请选择您的性别</option>
          <option value="男">男</option>
          <option value="女">女</option>
        </select>
    </div>

    <div class="facial">
        <img src="../../assets//images/圆_笑脸_line.png" width="100px" height="100px" alt="face"><br>
        <span>人脸识别</span>
    </div>
    <span class="text">备注</span><br><input type="text" placeholder="请输入文本" class="input2"
        id="remarkInput" v-model="formData.remark"><br>
    <button type="submit" class="button1" id="submitButton" @click="submitEvent()">提交</button>
    <button type="reset" class="button2" id="resetButton" @click="resetForm()">重新填写</button>

    <CreditScoreItem :resData="resData"/>
  </div>
</template>

<script>
import axios from 'axios'
import CreditScoreItem from '@/components/CreditScoreItem.vue'
// import { eventBus } from '../../services/eventBus'
export default {
  name: 'AuthForm',
  components: {
    CreditScoreItem
  },
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
      ],
      formData: {
        username: '',
        name: '',
        sex: '',
        remark: ''
      }
    }
  },
  methods: {
    // 搜索事件表单提交事件
    submitEvent () {
      axios.post('服务器地址', this.formData)
        .then(response => {
          this.resData = response.data
          this.sendResData()
        })
        .catch(error => {
          console.log('没有响应到该用户数据')
          console.error(error)
        })
    },
    // 重置表单
    resetForm () {
      this.formData = {
        username: '',
        name: '',
        sex: '',
        remark: ''
      }
    }
    // sendResData () {
    //   eventBus.$emit('sendresData', this.resData)
    // }
    // beforeDestroy () {
    //   this.$store.dispath('updatesharedresData', this.resData)
    // }
  }
}
</script>

<style scoped>
    .content {
        width: 800px;
        position: absolute;
        top: 140px;
        right: 250px;
        font-size: 18px;
    }

    .content .sign {
        color: #ff0000;
        font-size: 18px;
    }

    .content .input1 {
        width: 200px;
        height: 30px;
        border: solid 1px #fcfcfc;
        color: #ffffff;
        background-color: #202e4d;
        border-radius: 6px;
        margin-bottom: 15px;
    }

    #genderlist {
        width: 205px;
        height: 34px;
        background-color: #202e4d;
        color: #ffffff;
        border-radius: 6px;
        margin-bottom: 20px;

    }

    .sex {
        position: absolute;
        top: 1px;
        right: 100px;
    }

    .facial {
        border: dashed #fcfcfc 2px;
        border-radius: 6px;
        text-align: center;
        padding: 15px;
        width: 600px;
        margin-bottom: 15px;
    }

    .content .input2 {
        width: 635px;
        height: 50px;
        background-color: #202e4d;
        color: #fff;
        margin-bottom: 15px;
        border-radius: 6px;
        border: solid 1px #fcfcfc;
    }

    .button1 {
        width: 80px;
        height: 35px;
        text-align: center;
        border: none;
        border-radius: 5px;
        background-color: #34CEFF;
        color: white;
        font-size: 17px;
        cursor: pointer;
        margin-right: 10px;
    }

    .button2 {
        width: 80px;
        height: 35px;
        text-align: center;
        border: none;
        border-radius: 5px;
        background-color: #fcfcfc;
        color: #000;
        font-size: 17px;
        cursor: pointer;
        margin-bottom:20px ;
    }
</style>
