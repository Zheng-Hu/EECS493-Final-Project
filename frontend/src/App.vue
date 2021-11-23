<template>
    <div id="app">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="row m-1 w-100">
                <div class="col-1">
                    <a class="navbar-brand m-2">RunBlue</a>
                </div>
                <div class="col-10"></div>
                <div class="col-1">
                    <button v-if="this.$currentUser.username !== ''" v-on:click="logoutUser" class="btn btn-secondary">logout</button>
                </div>
            </div>
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
