import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    sharedresData: []
  },
  getters: {
    getsharedresData: state => state.sharedresData
  },
  mutations: {
    setsharedresData (state, data) {
      state.sharedresData = data
    }
  },
  actions: {
    updatesharedresData ({ commit }, data) {
      commit('setsharedresData', data)
    }
  },
  modules: {
  }
})
