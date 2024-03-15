<template>
    <div class="row">
        <div class="col">
            <h3>Productos</h3>
        </div>
    </div>
    <div class="row">
        <div class="col-2">
            <table class="table table-sm table-bordered">
                <thead class="table-dark">
                    <tr>
                        <th>Descripción</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-if="list_products.length === 0">
                        <td colspan="4">No hay Datos</td>
                    </tr>
                    <tr v-for="category in list_products" :key="category.id">
                        <td>{{ category }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script setup>
import { onMounted, ref } from 'vue'

const list_products = ref([])
const loading = ref(false)

onMounted(() => {
    loading.value = true;
    list_products.value = []
    let url = `${process.env.API_URL}/products`
    fetch(url)
        .then(resp => resp.json())
        .then(data => {
            list_products.value = data.results
            // loading.value = false;
        })
})
</script>
<style></style>