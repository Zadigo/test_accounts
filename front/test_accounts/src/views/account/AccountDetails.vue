<template>
    <section class="section">
        <div class="row">
            <div class="col s12 m3 l3">
                <SideBar></SideBar>
            </div>

            <div class="col s12 m6 l6">
                <div class="card-panel">
                    <form id="account_details">
                        <div class="input-field">
                            <input type="text" name="name" id="name" placeholder="Nom">
                        </div>
                        <div class="input-field">
                            <input type="text" name="surname" id="surname" placeholder="Prénom">
                        </div>
                        <div class="input-field">
                            <input type="email" name="email" id="email" placeholder="Email">
                        </div>
                        <div class="input-field">
                            <input type="date" name="date_of_birth" id="date_of_birth">
                        </div>
                        <button type="submit">Sauvegarder</button>
                    </form>
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
    }
}
</script>
