<template>
    <section class="section">
        <div class="container">
            <div class="row">
                <div class="col s12 m4 l4">
                    <!-- MENU -->
                    <SideMenu />
                </div>

                <div class="col s12 m8 l8">
                    <!-- MAIN -->
                    <MainForm v-bind:fields="fields" v-bind:id="id" />
                    <!-- SECONDARY -->
                    <SecondaryForm v-bind:fields="secondaryFields" v-bind:id="id" />
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import SideMenu from "@/components/account/SideMenu.vue"
import Form from "@/components/account/Form.vue"
import router from "../../../router"

export default {
    components: {
        SideMenu: SideMenu,
        MainForm: Form,
        SecondaryForm: Form
    },

    data() {
        return {
            id: 'test',
            fields: [
                {
                    "id": 1,
                    "type": "text",
                    "name": "name",
                    "model": "new_items.name"
                },
                {
                    "id": 1,
                    "type": "text",
                    "name": "surname",
                    "model": "new_items.name"
                }
            ],

            secondaryFields: [
                {
                    "id": 1,
                    "type": "text",
                    "name": "address",
                    "model": ""
                }
            ]
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
