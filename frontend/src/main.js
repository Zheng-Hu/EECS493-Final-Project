import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false

// Set global of current user
class CurrentUser {
    get username() {
        return this._username;
    }

    set username(newUser) {
        this._username = newUser;
    }

    constructor() {
        this._username = '';
    }
}

Vue.prototype.$currentUser = new CurrentUser();

// Use Axios
Vue.use(VueAxios, axios);

// Create vue instance
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
