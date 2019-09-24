<template>
    <img :src="product.url" :alt="product.id" class="responsive-img">
</template>

<script>
export default {
    props: ["product"]
}
</script>

<style>

</style>