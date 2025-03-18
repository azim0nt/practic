<script setup>
import { RouterView } from 'vue-router';


import Header from './components/Header.vue'
import Footer from './components/Footer.vue';


</script>

<template>
<div class="app">
    <div class="app-wrapper">
        <Header/>
        <RouterView/>
        <Footer/>
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
   

