<template>
<div class="row">
    <div class="col s12 l5 offset-l3">
        <div class="card">
            <div class="card-content">
                <form v-on:submit.prevent="loginUser">
                    <div class="input-field">
                        <input v-model="crendentials.email" type="text" name="email" id="email" autocomplete="email">
                    </div>
                    <div class="input-field">
                        <input v-model="crendentials.password" type="password" name="password" id="password" autocomplete="password">
                    </div>

                    <button type="submit" class="btn">Login</button>
                </form>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
    props: ['inputs'],

    data() {
        return {
            crendentials: {
                email: '',
                password: ''
            }
        }
    },

    methods: {
        loginUser: function() {
            this.$emit('loginUser', this.$data.crendentials)
        }
    }
}
</script>
