<template>
    <div class="card-panel">
        <h5>Prix</h5>
        <p class="range-field">
            <input @change="price" type="range" id="price_selector" min="0" max="100" />
        </p>
    </div>
</template>

<script>
export default {
    methods: {
        price: function() {
            var selectedPrice = $("#price_selector").val()
            this.$emit('price', selectedPrice)
        }
    }
}
</script>
