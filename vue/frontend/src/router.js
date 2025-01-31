import { createRouter, createWebHistory } from 'vue-router'

import Home from './views/Home.vue'
import TestRouter from './views/TestRouter.vue'

const routes = [
    {
        path:'/',
        component:Home,
    },
    {
        path:'/test-router',
        component:TestRouter
    },
]

const router = createRouter({history:createWebHistory(),routes})

export default router;