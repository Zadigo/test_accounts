<template>
    <section class="section">
        <div class="row">
            <div class="col s12 m3 l3">
                <SideBar></SideBar>
            </div>

            <div class="col s12 m6 l6">
                <div class="card-panel">
                    <h4>Ajouter une adresse</h4>
                    <button @click="addAddress()" class="btn" id="add_address">Add</button>
                </div>
            </div>

            <div v-show="hasAddresses" class="col s12 m6 l6" id="addresses">
                <!-- FORMS -->
            </div>
        </div>
    </section>
</template>

<script>
import SideBar from '@/components/account/SideBar.vue'

export default {
    data() {
        return {
            hasAddresses: false,
            addressInputs: {
                address: ''
            }
        }
    },

    components: {
        SideBar
    },

    methods: {
        addAddress: function() {
            var addressesSection = $('#addresses')
            var newForm = $('\
                <div class="card-panel">\
                    <form method=\"POST\" id=\"address\">\
                        <div class=\"input-field\">\
                            <input v-bind=\"addressInputs.address\" type=\"text\" name=\"address\" id=\"address\" placeholder=\"Address\">\
                        </div>\
                        <button type=\"submit\" class=\"btn white black-text z-depth-0\">\
                            <i class=\"material-icons left\">check</i> Modifier\
                        </button>\
                        <button type=\"submit\" class=\"btn white black-text z-depth-0\">\
                            <i class=\"material-icons left\">delete</i> Supprimer\
                        </button>\
                    </form>\
                </div>'
            )
            // The person now supposedly has an address
            this.$data.hasAddresses = true
            // Append new form item
            addressesSection.append(newForm);
        },

        deleteAddress: function() {
            // pass
        }
    },

    created() {
        document.title = 'Adress book | Company'
    }
}
</script>
