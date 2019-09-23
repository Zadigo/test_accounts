<template>
    <section class="section" id="products">
        <div class="container">
            <div class="row">
                <div class="col s12 m3 l3">
                    <!-- FILTERS -->
                    <FilterOne v-on:filterProducts="applyFilter" />

                    <PriceFilter v-on:price="productsWithPrices" />
                </div>

                <div class="col s12 m9 l9">
                    <Cards v-for="product in displayedProducts" :key="product.id" v-bind:product="product" />
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import Cards from "../../components/products/Cards.vue"
import FilterOne from "../../components/products/FilterOne.vue"
import PriceFilter from "../../components/products/PriceFilter.vue"

export default {
    components: {
        Cards: Cards,
        FilterOne: FilterOne,
        PriceFilter: PriceFilter
    },
    
    data() {
        return {
            products: [
                {
                    "id": 1,
                    "name": "Jupe ciseau",
                    "slug": "jupe-ciseau",
                    "url": "https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/sq-sample17.jpg",
                    "price": 84,
                    "active": true,
                    "created_on": ""
                },
                {
                    "id": 2,
                    "name": "Jupe vuitta",
                    "slug": "jupe-vuitta",
                    "url": "https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/sq-sample16.jpg",
                    "price": 45,
                    "active": true,
                    "created_on": ""
                },
                {
                    "id": 3,
                    "name": "Jupe fashion",
                    "slug": "jupe-fashion",
                    "url": "https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/sq-sample13.jpg",
                    "price": 34,
                    "active": false,
                    "created_on": ""
                },
                {
                    "id": 4,
                    "name": "Jupe vida",
                    "slug": "jupe-vida",
                    "url": "https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/sq-sample11.jpg",
                    "price": 56,
                    "active": false,
                    "created_on": ""
                },
                {
                    "id": 5,
                    "name": "Jupe goora",
                    "slug": "jupe-goora",
                    "url": "https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/sq-sample10.jpg",
                    "price": 76,
                    "active": true,
                    "created_on": ""
                },
                {
                    "id": 6,
                    "name": "Jupe pura",
                    "slug": "jupe-pura",
                    "url": "https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/sq-sample6.jpg",
                    "price": 12,
                    "active": true,
                    "created_on": ""
                }
            ],
            // The previous filter that was applied
            previousFilteredProducts: [],
            // The current applied filter
            filteredProducts: []
        }
    },

    computed: {
        displayedProducts() {
            var products = this.$data.filteredProducts

            return products
        }   
    },

    mounted() {
        // Set filteredProducts to all 
        // available products to filter
        this.$data.filteredProducts = this.$data.products
    },

    methods: {
        applyFilter: function(param) {
            var products = this.$data.products
            var cache = this.$data.filteredProducts

            // Reset
            cache = []

            products.forEach(product => {
                if (param == 'active') {
                    if (product.active == true) {
                        cache.push(product)
                    }
                } else if (param == 'inactive') {
                    if (product.active == false) {
                        cache.push(product)
                    }
                } else {
                    cache.push(product)
                }
            })

            // Commit new data
            this.$data.filteredProducts = cache
        },

        productsWithPrices: function(price) {
            // var cache = this.$data.filteredProducts
            var products = this.$data.products
            var cache = products.filter(function(product) {
                return product.price <= price
            })
            
            // Store the previous filter in case
            // this.$data.previousFilteredProducts = cache
            
            // Apply the new filter
            this.$data.filteredProducts = cache

            // Reset cache
            cache = []
        }
    }
}
</script>
