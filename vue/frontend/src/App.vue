<script setup>
import Header from './components/Header.vue';
</script>

<template>
<div class="app-wrapper">
  <Header/>
</div>
</template>

<style lang="scss">
@use './assets/styles/settings.scss' as *;

.app-wrapper{
    background-color: $bg-color;

}   
</style>
