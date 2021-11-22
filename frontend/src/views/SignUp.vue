<template>
    <div class="container">
        <div class="row text-dark">
            <div class="col-xl-5 col-lg-6 col-md-8 col-sm-10 mx-auto form p-4">
                <h1 class="display-4 py-2 text-truncate text-center mb-3">Create an Account!</h1>
                <div class="px-2">
                    <form class="justify-content-center">
                        <div class="form-group mt-2">
                            <label>First Name</label>
                            <input type="text" class="form-control">
                        </div>
                        <div class="form-group mt-2">
                            <label>Last Name</label>
                            <input type="text" class="form-control">
                        </div>
                        <div class="form-group mt-2">
                            <label>Username</label>
                            <input type="text" class="form-control">
                        </div>
                        <div class="form-group mt-2">
                            <label>Password</label>
                            <input type="password" class="form-control">
                        </div>
                        <div class="form-group mt-2">
                            <label>Repeat Password</label>
                            <input type="password" class="form-control">
                        </div>
                        <button class="btn btn-primary mt-4">Create Account</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'SignUp'
}
</script>
