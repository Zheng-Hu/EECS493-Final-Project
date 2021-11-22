<template>
    <div>
        <div>
            <Navigator page="Post"/>
        </div>
        <div class="container">
            <div class="row text-dark">
                <div class="col-xl-5 col-lg-6 col-md-8 col-sm-10 mx-auto form p-4">
                    <h1 class="display-4 py-2 text-truncate text-center mb-3">Make a Post</h1>
                    <div class="px-2">
                        <form @submit.prevent="onSubmit" class="justify-content-center">
                            <div class="form-group mt-2">
                                <label>Caption</label>
                                <textarea v-model="caption" class="form-control"></textarea>
                            </div>
                            <div class="form-group mt-2">
                                <label>Distance</label>
                                <input v-model="distance" type="text" class="form-control">
                            </div>
                            <div class="form-group mt-2">
                                <label>Time</label>
                                <input v-model="time" type="text" class="form-control">
                            </div>
                            <div class="form-group mt-2">
                                <label>Image Upload</label>
                                <input type="file" @change="onFileUpload" class="form-control" multiple accept="image/*">
                            </div>
                            <div class="form-group">
                                <button class="btn btn-primary mt-4">Post</button>
                            </div>
                        </form>
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
    name: 'Post',
    data() {
        return {
            FILE: null,
            caption: '',
            distance: '',
            time: ''
        }
    },
    beforeCreate() {
        if(this.$currentUser.username === '') {
            this.$router.push({ path: '/' });
        }
    },
    methods: {
        onFileUpload (event) {
            this.FILE = event.target.files[0];
        },
        onSubmit() {
            // Make sure user is logged in 
            if (this.$currentUser.username === '') {
                console.log("No user logged in.");
                console.log(this.$currentUser.username);
                return;
            }

            // Get the form data
            const formData = new FormData();
            formData.append('file', this.FILE);
            formData.append('caption', this.caption);
            formData.append('distance', this.distance);
            formData.append('time', this.time);
            formData.append('owner', this.$currentUser.username);

            // Send API call
            this.axios.post('http://localhost:8080/api/v1/posts/', formData)
            .then(response => {
                // Successful post
                console.log(response);

                // Redirect to feed
                this.$router.push({ path: '/feed' });
            })
            .catch(function (error) {
                // API call failed
                console.log(error);

                // Handle error (TODO)
            });
        }
    },
    components: {
        Navigator
    }
}
</script>
