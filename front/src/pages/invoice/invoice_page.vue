<template>
    <div class="row">
        <div class="col">
            <!-- <div class="card">
                <div class="card-body">
                    <div class="row">
                        <div class="col">Fecha</div>
                        <div class="col">asdasd</div>
                    </div>
                </div>
            </div> -->
            <table class="table table-sm table-bordered caption-top">
                <caption>FACTURAS</caption>
                <thead class="table-dark">
                    <tr>
                        <th>#</th>
                        <th>Fecha</th>
                        <th>Factura</th>
                        <th>Mesero</th>
                        <th>Cajero</th>
                        <th>Zona</th>
                        <th>Productos</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-if="list_sales.length === 0">
                        <td colspan="4">No hay Datos</td>
                    </tr>
                    <tr v-for="sale in list_sales" :key="sale.id">
                        <td>
                            <AkCirclePlus class="cursor-pointer" />
                        </td>
                        <td>{{ sale.date_closed }}</td>
                        <td>{{ sale.id }}</td>
                        <td>{{ sale.waiter }}</td>
                        <td>{{ sale.cashier }}</td>
                        <td>{{ sale.zone }}</td>
                        <td align="right">{{ sale.products.length }}</td>
                        <td align="right">{{ formatNumber(sale.total) }}</td>
                    </tr>

                </tbody>
            </table>
        </div>
    </div>
</template>
<script setup>
import { onMounted, ref } from 'vue'
import { formatNumber } from '../../tools/utils.js'
import { AkCirclePlus } from "@kalimahapps/vue-icons";


const list_sales = ref([])
const loading = ref(false)
const detail = ref(false)


onMounted(() => {
    loading.value = true;
    list_sales.value = []
    let url = `${proces.env.API_URL}/sales`
    fetch(url)
        .then(resp => resp.json())
        .then(data => {
            list_sales.value = data.results
            console.log('data.results', data.results);

            loading.value = false;
        })
})

</script>
<style></style>