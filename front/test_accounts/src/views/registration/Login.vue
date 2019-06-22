<template>
    <section class="section">
        <!-- SOCIAL REGISTRATION -->
        {% if request.path == "/accounts/login/" or request.path == "/accounts/signup/" %}
                {% include "registration/social.html" %}
        {% endif %}

        <!-- FORM -->
        <FormItem 
            v-on:receiveEmit="runThat"
            v-bind:inputs="inputs" 
            v-bind:button_name="button_name">
        </FormItem>

        <div class="row">
            <div class="col s12 l5 offset-l3">
                {% block extra_registration_links %}{% endblock extra_registration_links %}
            </div>
        </div>
        <button @click="authenticate()" type="submit">Test</button>
    </section>
</template>

<script>
import FormItem from '@/components/registration/Form.vue'
import axios from 'axios'

export default {
    components:{
        FormItem
    },

    data() {
        return {
            inputs: [],
            button_name: ''
        }
    },

    created() {
        this.$data.inputs = [
            {
                id: 1,
                type: 'email',
                name: 'email'
            },
            {
                id: 2,
                type: 'password',
                name: 'password'
            }
        ]
        this.$data.button_name = "Se connecter"
    },

    methods: {
        runThat: function(text) {
            console.log(text)
        },

        authenticate: function(data) {
            data={
                 "email": "zadigo@gmail.com",
                 "password": "touparet"
            }
            // axios.defaults.headers['Access-Control-Request-Headers']='Origin'
            axios.post(this.$store.state.endpoints.obtainJWT, data)
                .then((response) => {
                    this.$store.commit('updateToken', response.data.token)

                    var headers = {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        "Content-Type": "application/json"
                    }

                    this.$router.push('home')
                })
                .catch((error) => {
                    console.log(error);
                    console.debug(error);
                    console.dir(error);
                })
        }
    }
}
</script>
