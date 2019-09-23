<template>
    <div class="card-panel">
        <p>
            <label>
                <input @click="filterProducts('all')" type="radio" name="test" id="all" checked>
                <span>All</span>
            </label>
        </p>
        <p>
            <label>
                <input @click="filterProducts('active')" type="radio" name="test" id="active">
                <span>Active</span>
            </label>
        </p>
        <p>
            <label>
                <input @click="filterProducts('inactive')" type="radio" name="test" id="inactive">
                <span>Inactive</span>
            </label>
        </p>
    </div>
</template>

<script>
export default {
    methods: {
        filterProducts: function(param) {
            this.$emit('filterProducts', param)
        }
    }
}
</script>
