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
    </section>
</template>

<script>
import FormItem from '@/components/registration/Form.vue'

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
                type: 'text',
                name: 'nom'
            },
            {
                id: 2,
                type: 'text',
                name: 'prenom'
            },
            {
                id: 3,
                type: 'email',
                name: 'email'
            },
            {
                id: 4,
                type: 'password',
                name: 'password'
            }
        ]
        this.$data.button_name = "Créer"
    },

    methods: {
        runThat: function(text) {
            console.log(text)
        }
    }
}
</script>
