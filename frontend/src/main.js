import Vue from 'vue'
import VeeValidate from 'vee-validate'

import './styles/main.scss'
import App from './App.vue'
import router from './routes'

Vue.use(VeeValidate)

new Vue({
    el: '#app',
    router,
    template: '<App />',
    components: {App},
})