<template>
    <section class="section">
        <!-- SOCIAL REGISTRATION -->
        {% if request.path == "/accounts/login/" or request.path == "/accounts/signup/" %}
                {% include "registration/social.html" %}
        {% endif %}

        <!-- FORM -->
        <LoginForm v-on:loginUser="authenticate" />

        <div class="row">
            <div class="col s12 l5 offset-l3">
                {% block extra_registration_links %}{% endblock extra_registration_links %}
            </div>
        </div>
        <button @click="authenticate()" type="submit">Test</button>
    </section>
</template>

<script>
import LoginForm from '@/components/registration/LoginForm.vue'
import axios from 'axios'

export default {
    components:{
        LoginForm
    },

    data() {
        return {
            
        }
    },

    // created() {
    //     this.$data.inputs = [
    //         {
    //             id: 1,
    //             type: 'email',
    //             name: 'email'
    //         },
    //         {
    //             id: 2,
    //             type: 'password',
    //             name: 'password'
    //         }
    //     ]
    //     this.$data.button_name = "Se connecter"
    // },

    methods: {
        authenticate: function(credentials) {
            var tokenURL = this.$store.state.endpoints.obtainJWT

            axios.post(tokenURL, credentials)
                .then((response) => {
                    this.$store.commit('updateToken', response.data.token)

                    // var headers = {
                    //     "Authorization": `JWT ${this.$store.state.jwt}`,
                    // }

                    this.$router.push('home')
                })
                .catch((error) => {
                    
                })
        }
    }
}
</script>
