<template>
    <div class="container">
        <div class="row text-dark">
            <div class="col-xl-5 col-lg-6 col-md-8 col-sm-10 mx-auto form p-4">
                <h1 class="display-5 py-2 text-truncate text-center mb-3">Welcome to RunBlue!</h1>
                <div class="px-2">
                    <form @submit.prevent="onSubmit" class="justify-content-center">
                        <div class="form-group mt-2">
                            <label class="sr-only">Username</label>
                            <input v-model="username" type="text" class="form-control">
                        </div>
                        <div class="form-group mt-2">
                            <label class="sr-only">Password</label>
                            <input v-model="password" type="password" class="form-control">
                        </div>
                        <div v-if="error !== ''">
                            <p class="text-danger">{{ error }}</p>
                        </div>
                        <div class="mt-4">
                            <button class="btn btn-primary mx-1">Log In</button>
                            <router-link class="btn btn-warning mx-1" to="/signup">Sign Up</router-link>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            username: '',
            password: '',
            error: ''
        }
    },
    beforeCreate() {
        if(this.$currentUser.username !== '') {
            this.$router.push({ path: '/feed' });
        }
    },
    methods: {
        onSubmit() {
            // Call API
            this.axios({
                method: 'post',
                url: 'http://localhost:8080/api/v1/accounts/login/',
                data: {
                    username: this.username,
                    password: this.password
                }   
            })
            .then(response => {
                // User logged in successfully
                console.log(response);

                // Set global user variable
                this.$currentUser.username = this.username;

                // Reroute to feed
                this.$router.push({ path: '/feed' });

                // Remove error
                this.error = '';
            })
            .catch(error => {
                // API call failed
                if(error.response.status === 401) {
                    // Incorrect password
                    this.error = 'Incorrect password';
                }
                else if(error.response.status === 404) {
                    // User does not exist
                    this.error = 'Username does not exist';
                }
                else {
                    // Unknown error
                    console.log(error);
                }
            });
        }
    }
}
</script>
