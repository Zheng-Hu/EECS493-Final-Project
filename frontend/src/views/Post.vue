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
                        <form class="justify-content-center">
                            <div class="form-group mt-2">
                                <label>Caption</label>
                                <textarea class="form-control"></textarea>
                            </div>
                            <div class="form-group mt-2">
                                <label>Distance</label>
                                <input type="text" class="form-control">
                            </div>
                            <div class="form-group mt-2">
                                <label>Time</label>
                                <input type="text" class="form-control">
                            </div>
                            <div class="form-group mt-2">
                                <label>Image Upload</label>
                                <input type="file" class="form-control" multiple accept="image/*">
                            </div>
                            <button class="btn btn-primary mt-4">Post</button>
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
  components: {
    Navigator
  }
}
</script>
