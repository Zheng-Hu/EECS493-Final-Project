import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'
import Feed from '../views/Feed.vue'
import Post from '../views/Post.vue'
import Leaderboard from '../views/Leaderboard.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/feed',
    name: 'Feed',
    component: Feed
  },
  {
    path: '/post',
    name: 'Post',
    component: Post
  },
  {
    path: '/leaderboard',
    name: 'Leaderboard',
    component: Leaderboard
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
