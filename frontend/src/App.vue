<template>
    <div id="app">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand m-2">RunBlue</a>
        </nav>
        <!--     INCLUDE FOR EASY ACCESS TO OTHER URLS    
        <div id="nav">
            <router-link to="/">Login</router-link> |
            <router-link to="/signup">SignUp</router-link> | 
            <router-link to="/feed">Feed</router-link> | 
            <router-link to="/leaderboard">Leaderboard</router-link> | 
            <router-link to="/post">Post</router-link>
        </div> -->
        <router-view/>
    </div>
</template>
