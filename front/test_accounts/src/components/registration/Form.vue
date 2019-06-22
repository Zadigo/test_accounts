<template>
<div class="row">
    <div class="col s12 l5 offset-l3">
        <div class="card">
            <div class="card-content">
                <form v-on:submit.prevent="testEmit">
                    <div v-for="input in inputs" :key="input.id" class="input-field">
                        <input :type="input.type" :name="input.name" :id="input.name" :placeholder="input.name">
                    </div>
                    <button type="submit" class="btn">{{ button_name }}</button>
                </form>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
    props: ['inputs', 'button_name'],

    data() {
        return {
            new_input: {
                nom: '',
                prenom: '',
                email: '',
                password: ''
            }
        }
    },

    methods: {
        testEmit: function() {
            this.$emit('receiveEmit', 'Yes!!')
        }
    }
}
</script>
