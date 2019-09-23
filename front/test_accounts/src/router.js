import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Profile from './views/account/profile/Profile.vue'
import Login from './views/registration/Login.vue'
import Signup from './views/registration/Signup.vue'
import MyData from './views/account/profile/MyData.vue'
import PaymentMethods from './views/account/profile/PaymentMethods.vue'
import PasswordChange from './views/account/profile/PasswordChange.vue'
import Cart from './views/cart/Cart.vue'
import Product from './views/product/Product.vue'
import Products from './views/products/Products.vue'

// import AccountDetails from './views/account/AccountDetails.vue'
// import AddressBook from './views/account/AddressBook.vue'
// import MyOrders from './views/account/MyOrders.vue'

Vue.use(Router)

// router.beforeEach((to, from, next) => {
//   console.log(to)
// })

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: {
        title: 'TEST',
        metaTags: {
          name: 'TEST'
        }
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/signup',
      name: 'signup',
      component: Signup
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile,
      meta: {
        title: 'profile',
        metaTags: {
          name: 'profile'
        }
      }
    },
    {
      path: '/accounts/my-data',
      name: 'mydata',
      component: MyData
    },
    {
      path: '/account/password-change',
      name: 'password_change',
      component: PasswordChange
    },
    // {
    //   path: '/account/details',
    //   name: 'account_details',
    //   component: AccountDetails
    // },
    // {
    //   path: '/account/address-book',
    //   name: 'address_book',
    //   component: AddressBook
    // },
    // {
    //   path: '/account/social',
    //   name: 'social_accounts',
    //   component: AddressBook
    // },
    // {
    //   path: '/account/my-orders',
    //   name: 'my_orders',
    //   component: MyOrders
    // },
    // ,
    {
      path: '/account/payment-methods',
      name: 'payment_methods',
      component: PaymentMethods
    },
    {
      path: '/shop',
      name: 'shop',
      component: Products
    },
    {
      path: '/shop/:id/:slug',
      name: 'shop_product',
      component: Product
    },
    {
      path: '/cart',
      name: 'cart',
      component: Cart
    }
  ]
})
