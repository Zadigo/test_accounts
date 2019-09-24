<template>
    <section class="section" id="product">
        <div class="container">
            <div class="row">
                <div class="col s12 m2 l2">
                    <Pictures v-bind:images="images" />
                </div>
                <div class="col s12 m6 l6">
                    <Middle v-bind:product="product" />
                </div>
                <div class="col s12 m4 l4">
                    <Information />
                </div>
            </div>

            <div class="row">
                Another thing
            </div>
        </div>
    </section>
</template>

<script>
import Information from "../../components/product/classic/Information.vue"
import Middle from "../../components/product/classic/Middle.vue"
import Pictures from "../../components/product/classic/Pictures.vue"

export default {
    components: {
        Information,
        Middle,
        Pictures
    },

    data() {
        return {
            product: {
                "id": 1,
                "url": "https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/sq-sample17.jpg",
                "pictures": [
                    "https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/sq-sample17.jpg",
                    "https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/sq-sample17.jpg",
                    "https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/sq-sample17.jpg"
                ]
            },
            images: []
        }
    },

    mounted() {
        this.$data.images = this.$data.product.pictures
    }
}
</script>

<style lang="scss" scoped>

</style>
