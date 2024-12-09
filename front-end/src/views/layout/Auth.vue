<template>
  <div class=content>
    <span class="sign">*</span>用户名<br><input type="text" placeholder="请输入您的用户名" class="input1"
        id="usernameInput" v-model="formData.username"><br>

    <div class="facial">
        <img src="../../assets//images/圆_笑脸_line.png" width="100px" height="100px" alt="face"><br>
        <span>人脸识别</span>
    </div>
    <span class="text">备注</span><br><input type="text" placeholder="请输入文本" class="input2"
        id="remarkInput" v-model="formData.remark"><br>
    <button type="submit" class="button1" id="submitButton" @click="submitEvent()">提交</button>
    <button type="reset" class="button2" id="resetButton" @click="resetForm()">重新填写</button>
    <input type="text" class="button3" id="searchResData" placeholder="请输入文本进行搜索" @click="searchData()">
    <CreditScoreItem :resData="resData"/>
  </div>
</template>

<script>
import axios from 'axios'
import CreditScoreItem from '@/components/CreditScoreItem.vue'
import _ from 'lodash'

export default {
  name: 'AuthForm',
  components: {
    CreditScoreItem
  },
  data () {
    return {
      resData: [],
      templeData: [],
      formData: {
        nickname: '',
        username: '',
        remark: ''
      }
    }
  },
  methods: {
    // 表单提交事件
    async submitEvent () {
      if (this.formData.username === '') {
        return
      }
      axios.post('http://127.0.0.1:5000/query', this.formData)
        .then(response => {
          if (Array.isArray(response.data) && response.data.length === 0) {
            alert('用户名不存在')
            this.formData.username = ''
            return
          }
          response.data.forEach(item => {
            this.resData.push(item)
          })
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
        nickname: '',
        remark: ''
      }
    },
    // 搜索数据
    searchData () {
      const inputElement = document.getElementById('searchResData')
      // 设置防抖handleInputDebounce
      const self = this
      this.templeData = _.cloneDeep(this.resData)
      const handleInputDebounce = _.debounce(function () {
        console.log(inputElement.value)
        if (inputElement.value === '') {
          self.resData = _.cloneDeep(self.templeData)
        } else {
          // 搜索数据
          self.resData = self.templeData.filter(item =>
            item.nickname.includes(inputElement.value) ||
            item.username.toLowerCase().includes(inputElement.value.toLowerCase()) ||
            item.credit_score.toString().includes(inputElement.value) ||
            item.remark.includes(inputElement.value))
        // 重置搜索结果
        }
        console.log(self.templeData[0].username)
      }, 300)
      // 监听搜索框输入
      inputElement.addEventListener('input', handleInputDebounce)
    }
  },
  mounted () {
    this.searchData()
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
    #searchResData {
        margin-left: 20px;
        margin-top: 0px;
        width: 200px;
        height: 34px;
        border: none;
        border-radius: 5px;
        background-color: #fffefe;
        color: #000;
        font-size: 17px;
        cursor:text;
    }
</style>
