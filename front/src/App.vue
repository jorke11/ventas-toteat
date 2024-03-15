<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">
        <img :src="logo" alt="" width="140" height="40">
      </router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" to="/invoice">Facturas</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/product">Productos</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/category">Categorias</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/waiter">Meseros</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/cashier">Cajeros</router-link>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
  <div class="container-fluid">
    <router-view />
  </div>
</template>

<script setup>
import logo from './images/toteat.png'
</script>

<style></style>
