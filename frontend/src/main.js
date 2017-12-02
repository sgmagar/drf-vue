import Vue from 'vue'
import './styles/main.scss'
import App from './App.vue'
import router from './routes'

new Vue({
    el: '#app',
    router,
    template: '<App />',
    components: {App},
})