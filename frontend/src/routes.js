import Vue from 'vue'
import VueRouter    from 'vue-router'

import Home        from './views/Home.vue'
import Signup        from './views/Signup.vue'
import Login        from './views/Login.vue'

Vue.use(VueRouter)

const routes = [
    {path: '/', name:'home', component: Home},
    {path: '/signup', name:'signup', component: Signup},
    {path: '/login', name:'login', component: Login},
]

export default new VueRouter({
    mode: 'history',
    routes,
    linkActiveClass: 'active'
})