<script setup>
import Header from './components/Header.vue'
import { RouterView } from 'vue-router';
</script>

<template>
<div class="app">
    <div class="app-wrapper">
        <Header/>
        <RouterView/>
    </div>
</div>
</template>

<style lang="scss">
.app{
    background-color: $bg-color;
    width: 100%;
    min-height: 100vh;
    .app-wrapper{
        margin: 0 auto;
        width: 100%;
        max-width: 1600px;
    }   
}


</style>
   