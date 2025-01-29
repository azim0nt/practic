<script setup>
import nft_1 from '@/assets/images/nft_1.png'
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

                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Home'
}
</script>
<style lang="scss" scoped>
// @use '../assets/styles/settings.scss' as *;

.home-wrapper{
    @include flex(row, space-between,center);
    width: 100%;
    height: 89vh;
    .left{
        
    }
}
</style>