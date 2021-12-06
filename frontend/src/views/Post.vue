<template>
    <div>
        <div>
            <Navigator page="Post"/>
        </div>
        <div class="container">
            <div class="row text-dark">
                <div class="col-xl-5 col-lg-6 col-md-8 col-sm-10 mx-auto form p-4">
                    <h1 class="display-5 py-2 text-truncate text-center mb-3">Post Workout</h1>
                    <div class="px-2">
                        <form @submit.prevent="onSubmit" class="justify-content-center">
                            <div class="form-group mt-2">
                                <label>Caption</label>
                                <textarea v-model="caption" class="form-control"></textarea>
                            </div>
                            <div class="row mt-2">
                                <div class="form-group col-md-9">
                                    <label>Distance (miles)</label>
                                    <input v-model="distance" @input="handleDistanceChange" type="text" class="form-control">
                                </div>
                                <div class="form-group col-md-3">
                                    <label>Points</label>
                                    <svg @click="infoClick" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-info-circle info" viewBox="0 0 16 16">
                                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                                        <path d="m8.93 6.588-2.29.287-.082.38.45.083c.294.07.352.176.288.469l-.738 3.468c-.194.897.105 1.319.808 1.319.545 0 1.178-.252 1.465-.598l.088-.416c-.2.176-.492.246-.686.246-.275 0-.375-.193-.304-.533L8.93 6.588zM9 4.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"/>
                                    </svg>
                                    <input disabled :placeholder="points" type="text" class="form-control">
                                </div>
                            </div>
                            <div class="form-group mt-2">
                                <label>Time (minutes)</label>
                                <input v-model="time" type="text" class="form-control">
                            </div>
                            <div class="form-group mt-2">
                                <label>Image Upload</label>
                                <input type="file" @change="onFileUpload" class="form-control" multiple accept="image/*">
                            </div>
                            <div v-if="error !== ''">
                                <p class="text-danger">{{ error }}</p>
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

<style>
    .info {
        margin-left: 0.4em;
        margin-bottom: 0.2em;
    }
</style>

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
            time: '',
            error: '',
            points: 0
        }
    },
    beforeCreate() {
        if(this.$currentUser.username === '') {
            this.$router.push({ path: '/' });
        }
    },
    methods: {
        isNumeric(str) {
            return !isNaN(str) && !isNaN(parseFloat(str))
        },
        onFileUpload (event) {
            this.FILE = event.target.files[0];
        },
        infoClick()
        {
            alert("The points for your post is calculated based on Distance! Earn points to climb the leaderboard!");
        },
        handleDistanceChange() {
            if(this.isNumeric(this.distance)) {
                this.points = Math.floor(Number(this.distance) * 1.44);
            }
            else {
                this.points = 0;
            }
        },
        onSubmit() {
            // Make sure user is logged in 
            if (this.$currentUser.username === '') {
                this.error = 'No user logged in';
                return;
            }

            // Validate form data
            if(this.caption === '' || this.distance === '' || this.time === '' || this.FILE === null) {
                this.error = 'Please fill in all fields';
                return;
            }

            // Check if distance or time are not numbers
            if(!this.isNumeric(this.distance))
            {
                this.error = 'Distance must be a number of miles';
                return;
            }
            
            if(!this.isNumeric(this.time))
            {
                this.error = 'Time must be a number of minutes';
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
            .catch(error => {
                // API call failed
                this.error = 'Post could not be made';
                console.log(error);
            });
        }
    },
    components: {
        Navigator
    }
}
</script>
