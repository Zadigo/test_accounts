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
                        <form method="POST" id="password-reset-form">
                            <div class="input-field">
                                <input type="password" name="current_password" id="current_password" placeholder="Current password">
                            </div>
                            <div class="input-field">
                                <input type="password" name="new_password" id="new_password" placeholder="New password">
                            </div>
                            <button type="submit" class="btn waves-effect waves-light light-blue lighten-1">
                                <i class="material-icons left">check</i> Modifier
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import SideMenu from '@/components/account/SideMenu.vue'

export default {
    components: {
        SideMenu
    }
}
</script>
