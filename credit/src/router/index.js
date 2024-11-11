import Vue from 'vue'
import VueRouter from 'vue-router'
import layout from '@/views/layout/'
// import AuthRegister from '@/views/layout/AuthRegister'
import AboutPro from '@/views/layout/AboutPro'
import AuthLogin from '@/views/layout/Auth'
import CreditHistory from '@/views/layout/CreditHistory'
import creditScore from '@/views/layout/creditScore'
import DashBoard from '@/views/layout/DashBoard'
import FaceEmotion from '@/views/layout/FaceEmotion'
import VoiceEmotion from '@/views/layout/VoiceEmotion'
import UniInformation from '@/views/layout/UniInformation'
import UserLogin from '@/views/UserLogin'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: layout,
    children: [
      { path: '/DashBoard', component: DashBoard },
      { path: '/UniInformation', component: UniInformation },
      { path: '/AuthLogin', component: AuthLogin },
      { path: '/CreditHistory', component: CreditHistory },
      { path: '/FaceEmotion', component: FaceEmotion },
      { path: '/VoiceEmotion', component: VoiceEmotion },
      { path: '/creditScore', component: creditScore },
      { path: '/AboutPro', component: AboutPro },
      { path: '/UserLogin', component: UserLogin }
    ],
    redirect: '/Dashboard'
  }
]

const router = new VueRouter({
  routes
})

export default router
