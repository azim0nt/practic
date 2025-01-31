<script setup>
import { ref } from 'vue'

import { AkArrowRight } from '@kalimahapps/vue-icons';

import nft_2 from '@/assets/images/nft_2.png'
import nft_3 from '@/assets/images/nft_3.png'
import nft_4 from '@/assets/images/nft_4.png'
import nft_5 from '@/assets/images/nft_5.png'



const cards = ref([
    { name: 'Lorem Ipsum', weth: 1.20, image: nft_2, ends: '01.34.45' },
    { name: 'Dolor sit amet', weth: 0.21, image: nft_3, ends: '01.34.45' },
    { name: 'Dignissim curabitu..', weth: 0.01, image: nft_4, ends: '58.44.45' },
    { name: 'Amet pellentesq..', weth: 0.55, image: nft_5, ends: '01.34.45' }
])
</script>

<template>
    <div class="hot-auctions-wrapper">
        <div class="hot-auctions-top">
            <div class="left">
                <p>Hot Auctions</p>
            </div>
            <div class="right">
                <a href="#">
                    <p>View all</p>
                    <AkArrowRight class="arrow" />
                </a>
            </div>
        </div>
        <div class="hot-auctions-content">
            <div class="cards">
                <div v-for="card in cards" :key="card.name" class="card">
                    <div class="image">
                        <img :src="card.image" :alt="card.name">
                    </div>
                    <div class="card-info">
                        <div class="top">
                            <p>{{ card.name }}</p>
                            <p>{{ card.weth }} Weth</p>
                        </div>
                        <div class="bottom">
                            <p>Ends in <span>{{ card.ends }}</span></p><button class="border-btn">Bid</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'HotAuctions'
}
</script>

<style lang="scss" scoped>
.hot-auctions-wrapper {
    margin-bottom: 150px;
    height: 100%;
    max-height: 550px;
    .hot-auctions-top {
        @include flex(row, space-between, center);
        margin-bottom: 30px;

        .left {
            p {
                font-size: 48px;
                line-height: 72px;
            }
        }

        .right {
            a {
                @include flex(row, center, center);
                cursor: pointer;

                p {
                    font-size: 24px;
                    font-weight: 600;
                    line-height: 36px;
                }

                svg {
                    font-size: 24px;
                }
            }
        }
    }

    .hot-auctions-content {
        .cards {
            @include flex(row, space-between, center, 30px);

            .card {
                max-width: 300px;
                width: 100%;

                .image {
                    width: 100%;
                    height: 315px;
                    border-radius: 10px;
                    overflow: hidden;

                    img {
                        width: 100%;
                        height: 100%;
                        object-fit: cover;
                    }
                }

                .card-info {
                    .top {
                        @include flex(row, space-between, center);
                        margin: 20px 0;
                        padding-bottom: 20px;
                        border-bottom: 1px solid $gray;

                        p {
                            font-size: 16px;
                            line-height: 24px;

                            &:first-child {
                                font-weight: 600;
                            }
                        }
                    }

                    .bottom {
                        @include flex(row, space-between, center);

                        p {
                            line-height: 24px;
                            font-size: 16px;
                            color: $gray;
                        }
                        button{
                            width: 73px;
                            height: 29px;
                            padding:0;
                            font-size: 16px;
                            line-height: 24px;
                        }
                    }
                }
            }
        }
    }
}
</style>