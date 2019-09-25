<template>
    <div class="information">
        <h4>Product title</h4>
        <p>245€</p>
        <p id="description">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Ab culpa dolore veritatis aliquam facere cumque unde vitae 
            saepe nam enim fuga officiis minus, quos nobis alias omnis nesciunt. 
            Amet, pariatur.
        </p>

        <button class="btn-large waves-effect wave-light" id="add_to_cart">
            <i class="material-icons left">shopping_cart</i>
            Ajouter au panier
        </button>
    </div>
</template>

<script>
export default {
    props: ['product']
}
</script>

<style>

</style>