<script setup>
import { ref } from 'vue'


import shieldCheck from '@/assets/icons/shield-check.png'
import archive from '@/assets/icons/archive.png'
import fileMedia from '@/assets/icons/file-media.png'
import rocket from '@/assets/icons/rocket.png'


const cards = ref([
    { title: 'Connect your wallet', image: shieldCheck },
    { title: 'Posuere urna, sit amet molestie leo', image: archive },
    { title: 'Semper pretium libero sed quam ac integer ut', image: fileMedia },
    { title: 'Lectus volutpat magna vitae in arcu', image: rocket },
])
</script>
<template>
    <div class="getting-started-wrapper">
        <div class="getting-started-top">
            <p>Getting started</p>
            <p>Eu, molestie commodo, enim pellentesque turpis integer sagittis</p>
        </div>
        <div class="getting-started-content">
            <div class="cards">
                <div v-for="(card, index) in cards" :key="index" class="card">
                    <div class="image">
                        <img :src="card.image" :alt="'image-' + index">
                    </div>
                    <p class="text">
                        {{ card.title }}
                    </p>
                </div>
            </div>
        </div>
        <div class="spot-light"></div>
    </div>
</template>

<script>
export default {
    name: ""
};
</script>

<style lang='scss' scoped>
.getting-started-wrapper {
    padding-bottom: 100px;
    position: relative;

    .getting-started-top {
        @include flex(column, center, center);
        margin-bottom: 100px;

        p {
            &:first-child {
                font-size: 48px;
                line-height: 72px;
            }

            &:last-child {
                font-size: 24px;
                line-height: 36px;
            }
        }
    }

    .getting-started-content {
        position: relative;
        z-index: 2;

        .cards {
            @include flex(row, space-between, center);

            .card {
                max-width: 170px;
                width: 100%;

                .image {
                    @include flex(row, center, center);
                    margin-bottom: 20px;
                    width: 150px;
                    height: 150px;
                    border-radius: 26px;
                    background: rgba(255, 255, 255, 0.09);
                    box-shadow: 2.01px -2.01px 20px 0px rgba(214, 214, 214, 0.17) inset, -3.013px 3.013px 3.013px 0px rgba(255, 255, 255, 0.39) inset;
                    backdrop-filter: blur(37.21466827392578px);
                }

                .text {
                    text-align: center;
                    font-size: 16px;
                    font-weight: 400;
                    line-height: 24px;
                }
            }
        }
    }

    .spot-light {
        position: absolute;
        left: 0;
        top: 50%;
        width: 100%;
        height: 50px;
        border-radius: 10px;
        background: var(--Linear-Purple-Blue-Style, linear-gradient(94deg, #9B51E0 2.84%, #3081ED 99.18%));
        filter: blur(100px);
    }
}
</style>