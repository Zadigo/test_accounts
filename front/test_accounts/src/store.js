import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authuser: {},
    isAuthenticated: false,
    jwt: localStorage.getItem('token'),
    endpoints: {
      obtainJWT: 'http://127.0.0.1:8000/api/v1/auth/obtain-token/',
      refreshJWT: 'http://127.0.0.1:8000/api/v1/auth/refresh-token/',
      baseUrl: 'http://127.0.0.1:8000/api/v1/'
    }
  },
  
  mutations: {
    setAuthUser(
      state, {
        authUser,
        isAuthenticated
      }
    ) {
      Vue.set(state, 'authUser', authUser)
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },

    updateToken(state, newToken) {
      localStorage.setItem('token', newToken)
      state.jwt = newToken
    },

    removeToken(state) {
      localStorage.removeItem('token');
      state.jwt = null;
    }
  },
  actions: {

  }
})
