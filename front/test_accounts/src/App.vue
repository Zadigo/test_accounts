<template>
  <div id="app">
    <NavItem></NavItem>

    <main>
      <router-view/>
    </main>
  </div>
</template>

<script>
import NavItem from '@/components/navs/Nav.vue'

export default {
  components: {
    NavItem
  }
}
</script>

