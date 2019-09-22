<template>
    <section class="section">
        <div class="container">
            <div class="row">
                <div class="col s12 m8 l8">
                    <!-- ADDRESS -->
                    <Address />

                    <!-- PROMO -->
                    <Promo />

                    <!-- DELIVERY -->
                    <Delivery />

                    <!-- PAYMENT -->
                    <Payment />
                </div>
            
                <div class="col s12 m4 l4">
                    <div class="card">
                        <div class="card-content">
                            Side
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import Address from "@/components/cart/Address.vue"
import Delivery from "@/components/cart/Delivery.vue"
import Payment from "@/components/cart/Payment.vue"
import Promo from "@/components/cart/Promo.vue"

export default {
    components: {
        Address,
        Delivery,
        Payment,
        Promo
    },

    mounted() {
        // Create Stripe script
        let stripeScript = document.createElement('script')
        stripeScript.setAttribute('src', 'https://js.stripe.com/v3/')
        document.head.appendChild(stripeScript)

        //     var Payment = (function(stripe_id) {
        //     var stripe = Stripe(stripe_id)
        //     var elements = stripe.elements()
            
        //     var style = {}

        //     var card = elements.create('card', {style: style})

        //     card.mount('#card-element')

        //     // var constructForm = function(fields) {
        //     //     var form = $('#personal_information_form')
        //     //     var htmlFields = []
        //     //     var fields = ['name', 'address', 'country', 'postal_code']

        //     //     fields.forEach(function(field) {
        //     //         var field = $('\
        //     //             <div class="input-field">\
        //     //                 <input type="text" name="' + field + '" id="' + field + '"placeholder="' + field + '">\
        //     //             </div>'
        //     //         )
                    
        //     //         form.append(field)
        //     //     })
        //     //     // return htmlFields
                
        //     // }

        //     var tokenHandler = function(data) {
        //         // {{token: {...}}}
        //         var token = data.token.id
        //         var form = $('#personal_information_form')

        //         // Set the token in the hidden field
        //         form.find('input[type="hidden"]').val(token)

        //         // Submit the form with all the
        //         // data that we just got from
        //         // the customer
        //         // form.submit()
        //         // Or create an AJAX to Django
        //         form.on('submit', function(e) {
        //             e.preventDefault()
                    
        //             // Combine both of the stripe data
        //             // forma data together in order to
        //             // some more complex handling in Python
        //             var formData = $(this).serialize()
        //             var stucturedData = {
        //                 form: formData,
        //                 stripe: data
        //             }
        //             // formData['stripeData'] = data['token']

        //             console.log(stucturedData)

        //             // $.ajax({
        //             //     type: "POST",
        //             //     url: "http://www.example.com",
        //             //     data: formData,
        //             //     dataType: "json",
        //             //     success: function (response) {
        //             //         console.log(response.data)
        //             //     },
        //             //     error: function(response) {
        //             //         console.error(response.error)
        //             //     }
        //             // });
        //         })

        //         form.submit()
        //     }

        //     var cardForm = function() {
        //         var form = $('#payment_form')
                
        //         form.on('submit', function(e) {
        //             e.preventDefault()
                    
        //             // Creates the token
        //             stripe.createToken(card).then(function(result) {
        //                 if (result.error) {
        //                     // Inform the customer that
        //                     // there was an error in the process
        //                     var errorElement = document.getElementById('card-errors')
                            
        //                     errorElement.textContent = result.error.message
        //                 } else {
        //                     // We can handle the token here
        //                     tokenHandler(result)
        //                 }
        //             });
        //         })
        //     }
            
        //     // constructForm()
        //     cardForm();
        // })

        // Payment('pk_test_eo8zzqww6iuVFzWmLQEJ4F7K')
    }
}
</script>
