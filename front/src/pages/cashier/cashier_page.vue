<template>
    <div class="row">
        <div class="col">
            <h3>Cajeros</h3>
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
                    <tr v-if="list_cashier.length === 0">
                        <td colspan="4">No hay Datos</td>
                    </tr>
                    <tr v-for="cashier in list_cashier" :key="cashier.id">
                        <td>{{ cashier }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script setup>
import { onMounted, ref } from 'vue'

const list_cashier = ref([])
const loading = ref(false)

onMounted(() => {
    loading.value = true;
    list_cashier.value = []
    let url = `http://localhost:8000/cashier`
    fetch(url)
        .then(resp => resp.json())
        .then(data => {
            list_cashier.value = data.results
            loading.value = false;
        })
})
</script>
<style></style>