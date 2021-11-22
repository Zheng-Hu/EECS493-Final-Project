<template>
    <div class="container">
        <div class="row text-dark">
            <div class="col-xl-5 col-lg-6 col-md-8 col-sm-10 mx-auto form p-4">
                <h1 class="display-4 py-2 text-truncate text-center mb-3">Log In!</h1>
                <div class="px-2">
                    <form class="justify-content-center">
                        <div class="form-group mt-2">
                            <label class="sr-only">Username</label>
                            <input type="text" class="form-control">
                        </div>
                        <div class="form-group mt-2">
                            <label class="sr-only">Password</label>
                            <input type="password" class="form-control">
                        </div>
                        <div class="mt-4">
                            <router-link class="btn btn-primary mx-1" to="/feed">Log In</router-link>
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
  name: 'Login'
}
</script>
