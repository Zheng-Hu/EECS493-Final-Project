<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Login</router-link> |
      <router-link to="/signup">SignUp</router-link> | 
      <router-link to="/feed">Feed</router-link> | 
      <router-link to="/leaderboard">Leaderboard</router-link> | 
      <router-link to="/post">Post</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
</style>