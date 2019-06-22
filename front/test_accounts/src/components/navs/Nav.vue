<template>
<div>
    <div class="navbar-fixed">
        <nav class="red darken-1">
            <div class="nav-wrapper">
                <div class="container">
                    <router-link to="/" class="brand-logo">Accounts</router-link>
                    <a href="#" data-target="mobile-demo" class="sidenav-trigger"><i class="material-icons">menu</i></a>
                    <ul id="nav-mobile" class="hide-on-med-and-down right">
                        <li>
                            <router-link :to="{'name': 'login'}">Login</router-link>
                        </li>
                        <li>
                            <router-link :to="{'name': 'signup'}">Signup</router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
    <!-- SIDENAV -->
    <SideNav></SideNav>
</div>
</template>

<script>
import SideNav from "@/components/navs/SideNav.vue"

export default {
    components: {
        SideNav
    }
}
</script>

