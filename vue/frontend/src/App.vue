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

.app-wrapper{
    background-color: $bg-color;
    padding: 0  100px;
}   


</style>
   