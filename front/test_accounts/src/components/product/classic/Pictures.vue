<template>
    <div>
        <img v-for="image in images" :key="image" :src="image" :alt="image" class="responsive-img">
    </div>
</template>

<script>
export default {
    props: ["images"]
}
</script>

<style>

</style>