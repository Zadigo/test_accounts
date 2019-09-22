<template>
    <div class="card-panel">
        <form @submit.prevent="" method="POST" :id="id">
            <div v-for="f in fields" :key="f.name" class="input-field">
                <input v-model="new_items.name" :type="f.type" :name="f.name" :id="f.name">
            </div>
            <button class="btn waves-effect waves-light">
                <i class="material-icons left">check</i>
                Valider
            </button>
        </form>
    </div>
</template>

<script>
export default {
    props: ['fields', 'id'],
    data() {
        return {
            new_items: {
                name: ""
            }
        }
    },
    methods: {

    }
}
</script>
