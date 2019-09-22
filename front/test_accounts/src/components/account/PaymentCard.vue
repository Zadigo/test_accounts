<template>
    <div class='card-panel'>
        <div class='row'>
            <div class='col s12 m2 l2'>\
                <i class='material-icons'>credit_card</i>
            </div>
            <div class='col s12 m8 l8'>
                <p>Visa ({{ details.number }})</p>
                <p>Exp: {{ details.expmonth }}/{{ details.expyear }}</p>
                <p>{{ details.name }}</p>
            </div>
            <div class='col s12 m2 l2'>
                <i class='material-icons'>delete</i>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['details']
}
</script>
