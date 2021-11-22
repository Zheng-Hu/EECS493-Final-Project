<template>
    <div class="container text-center mt-3">
        <div class="row justify-content-center">
            <div class="col-sm-2">
                <router-link to="/post" v-if="page == 'Post'" class="btn btn-warning">Make a Post</router-link>
                <router-link to="/post" v-else class="btn btn-secondary">Make a Post</router-link>
            </div>
            <div class="col-sm-2">
                <router-link to="/feed" v-if="page == 'Feed'" class="btn btn-warning">Feed</router-link>
                <router-link to="/feed" v-else class="btn btn-secondary">Feed</router-link>
            </div>
            <div class="col-sm-2">
                <router-link to="/leaderboard" v-if="page == 'Leaderboard'" class="btn btn-warning">Leaderboard</router-link>
                <router-link to="/leaderboard" v-else class="btn btn-secondary">Leaderboard</router-link>
            </div>
        </div>
        <hr />
    </div>
</template>

<script>
export default {
  name: 'Navigator',
  props: {
    page: String
  }
}
</script>