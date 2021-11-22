<template>
    <div>
          <div>
            <Navigator page="Feed"/>
        </div>
        <div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import Navigator from '@/components/Navigator.vue'

export default {
  name: 'Feed',
  components: {
    Navigator
  }
}
</script>
