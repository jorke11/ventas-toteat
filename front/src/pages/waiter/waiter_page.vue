<template>
    <div class="row">
        <div class="col">
            <h3>Meseros</h3>
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
                    <tr v-if="list_waiter.length === 0">
                        <td colspan="4">No hay Datos</td>
                    </tr>
                    <tr v-for="waiter in list_waiter" :key="waiter.id">
                        <td>{{ waiter }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script setup>
import { onMounted, ref } from 'vue'

const list_waiter = ref([])
const loading = ref(false)

onMounted(() => {
    loading.value = true;
    list_waiter.value = []
    let url = `http://localhost:8000/waiter`
    fetch(url)
        .then(resp => resp.json())
        .then(data => {
            list_waiter.value = data.results
            loading.value = false;
        })
})
</script>
<style></style>