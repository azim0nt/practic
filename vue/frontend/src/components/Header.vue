<script setup>
import {RouterLink} from 'vue-router'
</script>

<template>
    <div class="header-wrapper">
        <nav>
            <div class="left">
                <RouterLink to="/">GASLUR</RouterLink>
            </div>
            <div class="middle">
                <RouterLink to="/test-router">HOME</RouterLink>
                <a href="#">MY PROFILE</a>
                <a href="#">ACTIVITY</a>
                <a href="#">HOW IT WORKS</a>
            </div>
            <div class="right">
                <button class="border-btn">CREATE</button>
                <button class="transparent-btn">SIGN IN</button>
            </div>
        </nav>
    </div>
</template>
<script>
export default {
    name: 'Header'
}
</script>
<style lang="scss" scoped>
// @use '../assets/styles/settings.scss' as *;

.header-wrapper {
    height: 100px;
    nav {
        @include flex(row, space-between, center);
        padding: 10px 0;
        .left {
            a {
                @extend %text-gradient;
                font-size: 32px;  
                font-weight: 700;
            }
        }

        .middle {
            @include flex(row, center, center, 30px);

            a {
                font-size: 12px;
                color: $gray;
                font-weight: 500;
                position: relative;

                &::after {
                    content: '';
                    position: absolute;
                    bottom: -4px; 
                    left: 0;
                    width: 0;
                    height: 2px; 
                    background: $violet;
                    transition: width 0.3s ease; 
                    border-radius: 2px;
                }

                &:hover::after {
                    width: 100%; 
                }

                &:hover {
                    @extend %text-gradient;
                    font-weight: 700;
                }
            }
        }
    }
}
</style>