<template>
    <div class="row">
        <div class="col-2">
            <h2>Categorias</h2>
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
                    <tr v-if="list_category.length === 0">
                        <td colspan="4">No hay Datos</td>
                    </tr>
                    <tr v-for="category in list_category" :key="category.id">
                        <td>{{ category }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script setup>
import { onMounted, ref } from 'vue'

const list_category = ref([])
const loading = ref(false)

onMounted(() => {
    loading.value = true;
    list_category.value = []
    let url = `${process.env.API_URL}/category`
    fetch(url)
        .then(resp => resp.json())
        .then(data => {
            console.log('data--', data);

            list_category.value = data.results
            // loading.value = false;
        })
})
</script>
<style></style>