<template>
    <div class="container">
        <div class="row text-dark">
            <div class="col-xl-5 col-lg-6 col-md-8 col-sm-10 mx-auto form p-4">
                <h1 class="display-4 py-2 text-truncate text-center mb-3">Create an Account!</h1>
                <div class="px-2">
                    <form @submit.prevent="onSubmit" class="justify-content-center">
                        <div class="form-group mt-2">
                            <label>Username</label>
                            <input v-model="username" type="text" class="form-control">
                        </div>
                        <div class="form-group mt-2">
                            <label>Password</label>
                            <input v-model="password" type="password" class="form-control">
                        </div>
                        <div class="form-group mt-2">
                            <label>Repeat Password</label>
                            <input v-model="re_password" type="password" class="form-control">
                        </div>
                        <button class="btn btn-primary mt-4 mx-1">Create Account</button>
                        <router-link class="btn btn-secondary mt-4 mx-1" to="/">Log In</router-link>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            re_password: ''
        }
    },
    beforeCreate() {
        if(this.$currentUser.username !== '') {
            this.$router.push({ path: '/feed' });
        }
    },
    methods: {
        onSubmit() {
            // Make sure passwords match
            if(this.password !== this.re_password) {
                console.log("Passwords do not match.")
                return;
            }

            // Call API
            this.axios({
                method: 'post',
                url: 'http://localhost:8080/api/v1/accounts/',
                data: {
                    username: this.username,
                    password: this.password
                }   
            })
            .then(response => {
                // User created account successfully
                console.log(response);

                // Reroute to feed
                this.$router.push({ path: '/' });
            })
            .catch(function (error) {
                // API call failed
                console.log(error);

                // Handle error (TODO)
            });
        }
    }
}
</script>
