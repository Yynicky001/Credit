import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '@/style/common.less'
import axios from 'axios'
import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'
Vue.config.productionTip = false
Vue.prototype.$bus = new Vue()
Vue.prototype.axios = axios
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
