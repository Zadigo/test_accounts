<template>
    <div class="card-panel">
        <div class="collection">
            <a href="{% url 'profile' %}" class="collection-item">{% trans 'Profil' %}</a>
            <router-link :to="{'name': 'my_orders'}" class="collection-item">Mes commandes</router-link>
            <router-link :to="{'name': 'account_details'}" class="collection-item">Mes données</router-link>
            <router-link :to="{'name': 'password_change'}" class="collection-item">Mot de passe</router-link>
            <router-link :to="{'name': 'address_book'}" class="collection-item">Adresses</router-link>
            <router-link :to="{'name': 'payment_methods'}" class="collection-item">Paiements</router-link>
            <router-link :to="{'name': 'social_accounts'}" class="collection-item">Social</router-link>
        </div>
    </div>
</template>
