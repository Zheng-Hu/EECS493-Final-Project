<template>
    <div>
        <div>
            <Navigator page="Feed"/>
        </div>
        <div class="container w-50 mt-5">
            <div v-for="(post, index) in posts" :key="post.postid" :id="index" class="card mb-5">
                <div class="card-header">
                    <h5 class="mb-1">
                        {{ post.owner }}'s Run
                    </h5>
                </div>
                <img class="card-img" :src="'http://localhost:8080/media/' + post.imageurl" />
                <div class="card-body">
                    <div class="mb-3">
                        <div class="row">
                            <div class="col">
                                <div class="card-text">
                                    {{post.caption}}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col">
                            <p class="card-text text-muted text-weight-light">
                                Distance: {{post.distance}} miles
                            </p>
                        </div>
                        <div class="col">
                            <p class="card-text text-muted text-weight-light">
                                Time: {{post.time}} minutes
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import Navigator from '@/components/Navigator.vue'

export default {
    name: 'Feed',
    data: function () {
        return {
            posts: []
        }
    },
    created() {
        console.log(this.$currentUser.username);
        // Call API to get all posts
        this.axios({
            method: 'get',
            url: 'http://localhost:8080/api/v1/posts/'
        })
        .then(response => {
            // Successful API call, put posts into local variable
            this.posts = response.data.data;
            console.log(this.posts);
        })
        .catch(function (error) {
            // API call failed
            console.log(error);
        });
    },
    components: {
        Navigator
    }
}
</script>
