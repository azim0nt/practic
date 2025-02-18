import { createRouter, createWebHistory } from 'vue-router'

import Home from './views/Home.vue'
import TestRouter from './views/TestRouter.vue'
import NoPage from './views/NoPage.vue'

const routes = [
    {
        path:'/',
        component:Home,
    },
    {
        path:'/test-router',
        component:TestRouter
    },
    {
        path:'/:pathMath(.*)*',
        component:NoPage

    }
]

const router = createRouter({history:createWebHistory(),routes})

export default router;