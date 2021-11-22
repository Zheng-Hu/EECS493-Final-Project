<template>
    <div id="app">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand m-2">RunBlue</a>
            <button v-if="this.$currentUser.username !== ''" v-on:click="logoutUser" class="btn btn-secondary">logout</button>
        </nav>
        <router-view/>
    </div>
</template>

<script>
export default {
    methods: {
        logoutUser() {
            // Set curentUser to empty
            this.$currentUser.username = '';

            // Redirect to login page
            this.$router.push({ path: '/' });
        }
    }
}
</script>
