<script setup>
import nft_1 from '@/assets/images/nft_1.png'
import avatar from '@/assets/images/avatar.png'
import { CiHeart } from '@kalimahapps/vue-icons';
import HotAuctions from './HotAuctions.vue';
import GettingStarted from './GettingStarted.vue';
import Discover from './Discover.vue';
</script>

<template>
    <div class='home-wrapper'>
        <div class="left">
            <div class="text">
                <p class="title">Discover, collect, and charity in extraordinary NFT marketplace</p>
                <p class="subtitle">In aenean posuere lorem risus nec. Tempor tincidunt aenean purus purus vestibulum
                    nibh mi venenatis</p>
            </div>
            <div class="buttons">
                <button class="gradient-btn">Explore</button>
                <button class="border-btn">Create</button>
            </div>
        </div>
        <div class="right">
            <div class="card">
                <div class="image">
                    <img :src="nft_1" alt="NFT">
                </div>
                <div class="info">
                    <div class="owner">
                        <div class="avatar">
                            <img :src="avatar" alt="avatar">
                        </div>
                        <div class="owner-info">
                            <p>Laura</p>
                            <p>0.21 Weth</p>
                        </div>
                    </div>
                    <div class="card-info">
                        <p>WE ARE HERE</p>
                        <p>
                            <CiHeart class="heart" /> 25
                        </p>
                    </div>
                </div>
                <div class="spot-light purple"></div>
                <div class="spot-light blue"></div>
            </div>
        </div>
    </div>
    <HotAuctions />
    <GettingStarted />
    <Discover />
</template>
<script>
export default {
    name: 'Home'
}
</script>
<style lang="scss" scoped>
.home-wrapper {
    @include flex(row, space-between, center);
    width: 100%;
    height: 100%;
    max-height: 800px;
    margin-bottom: 150px;

    .left {
        width: 50%;
        ;

        .text {
            p {
                margin-bottom: 30px;

                &.title {
                    font-size: 72px;
                    font-weight: 600;
                    line-height: 82px;
                    max-width: 700px;
                }

                &.subtitle {
                    color: $text-color;
                    font-size: 24px;
                    font-weight: 400;
                    max-width: 700px;
                    line-height: 35px;

                }
            }
        }

        .buttons {
            button {
                padding: 0;
                width: 220px;
                height: 60px;
                font-size: 24px;
                font-weight: 600;
            }
        }
    }

    .right {
        .card {
            @include flex(column, space-between, stretch);
            width: 500px;
            height: 580px;
            border-radius: 20px;
            padding: 20px;
            position: relative;
            z-index: 1;
            /* From https://css.glass */
            background: rgba(255, 255, 255, 0.07);
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(156, 156, 156, 0.53);

            .info {
                @include flex(row, space-between, center);
                position: relative;
                z-index: 3;

                .owner {
                    display: flex;

                    .owner-info {
                        p {
                            &:first-child {
                                font-weight: 600;
                            }
                        }
                    }
                }

                .card-info {
                    p {
                        &:first-child {
                            font-weight: 600;
                        }

                        &:last-child {
                            @include flex(row, right, center, 5px);

                            svg {
                                font-size: 20px;
                            }
                        }
                    }
                }
            }

            .spot-light {
                width: 400px;
                height: 400px;
                position: absolute;
                z-index: -1;

                &.purple {
                    left: -150px;
                    top: -150px;
                    background: radial-gradient(circle, #fc37ff42 0%, rgba(0, 0, 0, 0) 70%);
                }

                &.blue {
                    right: -150px;
                    bottom: -150px;
                    background: radial-gradient(circle, #18B2DE42 0%, rgba(0, 0, 0, 0) 70%);
                }
            }
        }
    }
}
</style>