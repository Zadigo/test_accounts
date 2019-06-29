<template>
    <section class="section">
        <div class="row">
            <div class="col s12 m3 l3">
                <SideBar></SideBar>
            </div>

            <div class="col s12 m6 l6">
                <div class="card-panel">
                    <h4>Mes commandes</h4>
                </div>
            </div>

            <div v-if="hasOrders" class="col s12 m6 l6" id="orders">
                <div v-for="order in orders" :key="order.reference" class="card-panel">
                    <!-- DO SOMETHING -->
                </div>
            </div>

            <div v-else class="col s12 m6 l6" id="start_shopping">
                <div class="card-panel center">
                    <h4>You currently have no orders</h4>
                    <router-link :to="{'name': 'home'}" class="btn-large">Start shopping</router-link>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import SideBar from '@/components/account/SideBar.vue'

export default {
    components: {
        SideBar
    },

    data() {
        return {
            hasOrders: false,
            orders: []
        }
    },

    created() {
        console.log(this.$data.orders.length())
        // 1. Check if the customer has orders
        // this.$data.hasOrders = true
    }
}
</script>
