<script setup>
import { FeFilter } from '@kalimahapps/vue-icons';
import { LaSortAmountUpSolid } from '@kalimahapps/vue-icons';
import { CdArrowSmallUp } from '@kalimahapps/vue-icons';
import { ref } from 'vue'

import nft_6 from '@/assets/images/nft_6.png'
import nft_7 from '@/assets/images/nft_7.png'
import nft_8 from '@/assets/images/nft_8.png'
import nft_9 from '@/assets/images/nft_9.png'
import nft_10 from '@/assets/images/nft_10.png'
import nft_11 from '@/assets/images/nft_11.png'
import nft_12 from '@/assets/images/nft_12.png'
import nft_13 from '@/assets/images/nft_13.png'

const cards = ref([
    { name: 'Lorem Ipsum', weth: 1.20, image: nft_6, ends: '01.34.45' },
    { name: 'Dolor sit amet', weth: 0.21, image: nft_7, ends: '01.34.45' },
    { name: 'Dignissim curabitu..', weth: 0.01, image: nft_8, ends: '58.44.45' },
    { name: 'Amet pellentesq..', weth: 0.55, image: nft_9, ends: '01.34.45' },
    { name: 'Lorem Ipsum', weth: 1.20, image: nft_10, ends: '01.34.45' },
    { name: 'Dolor sit amet', weth: 0.21, image: nft_11, ends: '01.34.45' },
    { name: 'Dignissim curabitu..', weth: 0.01, image: nft_12, ends: '58.44.45' },
    { name: 'Amet pellentesq..', weth: 0.55, image: nft_13, ends: '01.34.45' }
])

</script>
<template>
    <div class="discover-wrapper">
        <div class="discover-top">
            <div class="left">
                <p>Discover</p>
            </div>
            <div class="right">
                <button>
                    <LaSortAmountUpSolid /> Category
                </button>
                <button>Cheapest
                    <CdArrowSmallUp class="arrow down" />
                </button>
                <button>Newest
                    <CdArrowSmallUp class="arrow" />
                </button>
                <button class="gradient-btn">
                    <FeFilter /> Filter
                </button>
            </div>
        </div>
        <div class="discover-content">
            <div class="cards">
                <div class="card" v-for="(card, i) in cards" :key="i">
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
    name: "Discover"
};
</script>

<style lang='scss' scoped>
.discover-wrapper {
    padding-bottom: 150px;

    .discover-top {
        @include flex(row, space-between, center);

        margin-bottom: 50px;

        .left {
            font-size: 48px;
            font-weight: 500;
            line-height: 72px;
        }

        .right {
            @include flex(row,center,center,30px);
            button {
                @include flex(row,center,center,5px);
                background-color: transparent;
                line-height: 36px;
                font-size: 24px;
                svg{
                    font-size: 34px;
                    &.down{
                        transform: rotate(180deg);
                    }
                }
            }
        }
    }

    .discover-content {
        .cards {
            @include grid(4, 30px, 300px);
            width: 100%;
            justify-content: space-between;

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

                        button {
                            width: 73px;
                            height: 29px;
                            padding: 0;
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