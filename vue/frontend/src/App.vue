<script setup>
import Header from './components/Header.vue'
import { RouterView } from 'vue-router';
</script>

<template>
<div class="app-wrapper">
    <Header/>
    <RouterView/>
</div>
</template>

<style lang="scss">
// @use './assets/styles/settings.scss' as *;

.app-wrapper{
    background-color: $bg-color;
    padding: 0  50px;
}   


</style>
   