<template>
    <section class="section">
        <div class="container">
            <div class="row">
                <div class="col s12 m4 l4">
                    <!-- MENU -->
                    <SideMenu />
                </div>

                <div class="col s12 m8 l8">
                    <div class="card-panel center">
                        <button @click="displayForm()" class="btn-large blue darken-3 waves-effect waves-light">
                            <i class="material-icons left">credit_card</i>
                            Ajouter un nouveau moyen
                        </button>
                    </div>

                    <div class="payment_cards"></div>

                    <div v-show="showForm" class="card-panel" id="form_add_new_method">
                        <form @submit.prevent="createNewCard()">

                            <div class="input-field">
                                <input v-model="details.number" type="text" name="card_number" id="card_number" placeholder="Card number" autocomplete="cc-number">
                            </div>
                            <div class="input-field">
                                <input v-model="details.cvv" type="text" name="cvv" id="cvv" placeholder="CVV" autocomplete="cc-csc">
                            </div>
                            <div class="input-field">
                                <select v-model="details.expmonth" name="expmonth" id="expmonth" autocomplete="cc-exp-month">
                                    <option v-for="value in values" :key="value" :value="value">{{ value }}</option>
                                </select>
                            </div>
                            <div class="input-field">
                                <select v-model="details.expyear"  name="expyear" id="expyear" autocomplete="cc-exp-year">
                                    <option v-for="value in getYear" :key="value" :value="value">{{ value }}</option>
                                </select>
                            </div>
                            <div class="input-field">
                                <input v-model="details.name" type="text" name="name" id="name" placeholder="Name">
                            </div>


                            <p>
                                <label>
                                    <input type="checkbox" name="default" id="default">
                                    <span>Définir comme méthode de paiement par défaut</span>
                                </label>
                            </p>
                            <button type="submit" class="btn">
                                <i class="material-icons left">check</i>Ajouter
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import PaymentCard from "@/components/account/PaymentCard.vue"
import SideMenu from "@/components/account/SideMenu.vue"
import Vue from 'vue'

export default {
    components: {
        SideMenu: SideMenu,
        PaymentCard: PaymentCard
    },

    data() {
        return {
            showForm: false,
            details: {
                "name": "",
                "number": "",
                "cvv": "",
                "expmonth": "",
                "expyear": ""
            },
            values: []
        }
    },

    methods: {
        displayForm: function() {
            this.$data.showForm = !this.$data.showForm
        },

        // Creates a new card by appending a
        // card to #payment_cards -- the stripe
        // request is performed in the backend
        createNewCard: function() {
            var componentClass = Vue.extend(PaymentCard)
            var instance = new componentClass(
                {
                    propsData: this.$data.details
                }
            )
            instance.$mount()
            this.$refs.container.appendChild(instance.$el)
        }
    },

    computed: {
        getYear: function() {
            var date = new Date()
            var currentYear = date.getFullYear()
            var years = []

            for (let i = 0; i < 6; i++) {
                years.push(currentYear + i)
            }
            return years
        }
    },

    mounted() {
        // var userLoggedIn = false

        // if (!userLoggedIn) {
        //     router.push({"name": "login", query:{"next": "profile"}})
        // }

        // Expiry month
        for (let i = 1; i < 13; i++) {
            this.$data.values.push(i)
        }
    }
}
</script>
