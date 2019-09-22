<template>
    <section class="section">
        <div class="container">
            <div class="row">
                <div class="col s12 m4 l4">
                    <!-- MENU -->
                    <SideMenu />
                </div>

                <div class="col s12 m8 l8">
                    <div class="card-panel">
                        <p>Gérer les comptes connectés avec Kurrikulam :</p>
                        <a href="#!" class="btn"><i class="fab fa-google left"></i>Google</a>
                        <a href="#!" class="btn disabled"><i class="fab fa-twitter left"></i>Twitter</a>
                        <a href="#!" class="btn disabled"><i class="fab fa-linkedin left"></i>LinkedIn</a>
                    </div>

                    <div class="card-panel">
                        <p>
                            Si vous ne souhaitez plus avoir de compte chez nous, 
                            vous pouvez utiliser le lien ci-dessous.
                        </p>

                        <!-- TRIGGER -->
                        <a class="waves-effect waves-light btn modal-trigger red darken-4" href="#modal1"><i class="material-icons left">remove_circle</i>Supprimer mon compte</a>
                    </div>

                </div>
            </div>
            <Modal />
        </div>
    </section>
</template>

<script>
import DeleteAccountModal from "@/components/account/DeleteAccountModal.vue";
import SideMenu from "@/components/account/SideMenu.vue"
import Form from "@/components/account/Form.vue"
import router from "../../../router"

export default {
    components: {
        SideMenu: SideMenu,
        MainForm: Form,
        SecondaryForm: Form,
        Modal: DeleteAccountModal
    },

    data() {
        return {

        }
    },

    mounted() {
        // var userLoggedIn = false

        // if (!userLoggedIn) {
        //     router.push({"name": "login", query:{"next": "profile"}})
        // }
    }
}
</script>
