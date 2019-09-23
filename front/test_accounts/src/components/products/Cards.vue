<template>
    <div class="col s12 m4 l4">
        <transition name="cards">
            <router-link :to="{name: 'shop_product', params:{id: product.id, slug: product.slug}}" class="card-link-wrapper">
                <div class="card special push-up-with-image">
                    <div class="card-image">
                        <img :src="product.url" :alt="product.name">
                    </div>
                    <div class="hover-cover-4">
                        <h5>{{ product.name }}</h5>
                    </div>
                </div>
            </router-link>
        </transition>
    </div>
</template>

<script>
export default {
    props: ["product"]
}
</script>

<style lang="scss" scoped>
.cards {
    &-enter-active {
        transition: opacity .6s ease-in-out;
    }
    
    &-enter {
        opacity: 0;
    }

    &-enter-to {
        opacity: 1;
    }
}

@mixin hover-cover {
    position: absolute;
}

.card-link-wrapper {
    color: inherit;
}

.card {
    &.special {
        cursor: pointer;
        overflow: hidden;

        * {
            transition: all .25s ease-in-out;
        }
        
        .card-image {
            max-height: 60%;
            overflow: hidden;
        }

        &:hover {
            &.dim .card-image img{
                opacity: 0.7;
            }

            &.push-up {
                .hover-cover-4 {
                    transform: translateY(-115px);
                }

                .hover-cover-icons {
                    transform: translateY(-295%);
                    color: inherit;

                    i {
                        &:hover {
                            background-color: black;
                            color: white;
                        }
                    }
                }
            }

            &.push-up-with-image {
                .card-image img {
                    transform: translateY(-55px);
                }

                .hover-cover-4 {
                    transform: translateY(-115px);
                }
            }

            &.zoom {
                .card-image img {
                    transform: scale(1.1, 1.1);
                }
            }

            .card-cover {
                opacity: .7;

                p {
                    opacity: 1;
                }
            }

            .ripple:after {
                content: "";
                display: block;
                position: absolute;
                width: 100%;
                height: 100%;
                top: 0;
                left: 0;
                pointer-events: none;
                background-image: radial-gradient(circle, #fff 10%, transparent 10.01%);
                background-repeat: no-repeat;
                background-position: 50%;
                -webkit-transform: scale(10, 10);
                        transform: scale(10, 10);
                opacity: 0;
                -webkit-transition: opacity 1s, -webkit-transform .5s;
                transition: opacity 1s, -webkit-transform .5s;
                transition: transform .5s, opacity 1s;
                transition: transform .5s, opacity 1s, -webkit-transform .5s;
              }
              
            .ripple:active:after {
                -webkit-transform: scale(0, 0);
                        transform: scale(0, 0);
                opacity: .3;
                -webkit-transition: 0s;
                transition: 0s;
            }
        }

        .hover-cover-4 {
            @include hover-cover();
            background-color: white;
            width: 100%;
            bottom: 0;
            padding: .75rem;
            bottom: -115px;
            text-align: center;

            p {
                margin-top: 0;
            }
        }

        .hover-cover-icons {
            @include hover-cover();
            left: 50%;
            right: 50%;
            bottom: -48px;
            display: flex;
            flex-direction: row;
            justify-content: center;
            z-index: 1;

            a {
                display: block;
                color: inherit;
                height: 25px;
                width: 25px;
            }

            a:not(:last-child) {
                margin-right: 32px;
            }

            a > i {
                background-color: white;
                line-height: 15px;
                padding: 15px;
            }
        }

        div.discount {
            position: absolute;
            top: 0;
            right: 0;
            font: {
                family: inherit;
                size: 14px;
                weight: 600;
            }
            padding: 15px;
            background-color: #ec407a;
            z-index: 1;    
            opacity: .85;
            color: white;
        }

        .card-cover {
            z-index:999;
            position:absolute;
            top:0;
            background-color:black;
            height: 100%;
            width: 100%;
            opacity: 0;
            padding: 25px;

            p {
                position:relative;
                color:white;
            }
        }
    }
}
</style>