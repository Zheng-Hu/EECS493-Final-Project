<template>
  <div>
      <h1>Navigator</h1>
      <h3>{{ page }}</h3>
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