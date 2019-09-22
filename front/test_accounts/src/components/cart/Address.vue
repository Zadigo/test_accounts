<template>
  <div class="card">
    <div class="card-content">
        <h5>Address</h5>
        <p v-if="!showInput">An address</p>
        <input v-show="showInput" type="text" name="address" id="address">

        <button @click="showInput = !showInput" v-if="address" class="btn">Modifier</button>
        <button v-show="showInput" class="btn">Ajouter</button>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            address: true,
            showInput: false
        }
    }
}
</script>
