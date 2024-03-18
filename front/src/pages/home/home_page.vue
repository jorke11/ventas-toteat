<template>
    <div class="row mt-2">
        <div class="col">
            <div class="row my-4">
                <div class="col-2" v-if="!loadingSync">
                    <button class="btn btn-info btn-sm" v-if="!loadingSync" @click="syncData">Sincronizar Datos</button>
                </div>
                <div class="col" v-else>
                    <div class="spinner-border" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <h3>Ventas del {{ title }}</h3>
                </div>
            </div>
            <div class="row my-4">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <h4>TOTAL: {{ formatNumber(total) }}</h4>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <h4>PROMEDIO POR DIA: {{ formatNumber(average) }}</h4>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <h4>PROMEDIO POR SEMANA: {{ formatNumber(averageWeek) }}</h4>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row" v-if="!loading">
        <div class="col-7">
            <div class="row d-flex justify-content-center">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <div class="card-title">Ventas de Productos por Monto</div>
                            <div class="row">
                                <div class="col">
                                    <table class="table table-sm table-bordered">
                                        <thead class="table-dark">
                                            <tr>
                                                <th>Productos</th>
                                                <th>Total</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="product in listSalesProduct">
                                                <td>{{ product[0] }}</td>
                                                <td align="right">{{ formatNumber(product[1]) }}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                <div class="col">
                                    <Bar id="my-chart-id" :options="chartOptions" :data="chartDataProduct" />
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <div class="card-title">Ventas Por Productos por Unidades</div>
                            <div class="row">
                                <div class="col">
                                    <table class="table table-sm table-bordered">
                                        <thead class="table-dark">
                                            <tr>
                                                <th>Productos</th>
                                                <th>Total</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="product in listSalesProductUnits">
                                                <td>{{ product[0] }}</td>
                                                <td align="right">{{ formatNumber(product[1]) }}</td>
                                            </tr>
                                        </tbody>
                                    </table>

                                </div>
                                <div class="col">
                                    <Bar id="my-chart-id" :options="chartOptions" :data="chartDataProductUnits" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <div class="row">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <div class="card-title">Ventas Por Categorias</div>
                            <div class="row">
                                <div class="col">
                                    <table class="table table-sm table-bordered">
                                        <thead class="table-dark">
                                            <tr>
                                                <th>Categoria</th>
                                                <th>Total</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="category in listSalesCategory">
                                                <td>{{ category[0] }}</td>
                                                <td align="right">{{ formatNumber(category[1]) }}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                <div class="col">

                                    <Pie :data="chartDataCategory" :options="chartOptions" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <div class="row my-2">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <div class="card-title">Ventas Por Meses</div>
                            <div class="row">
                                <div class="col">
                                    <table class="table table-sm table-bordered">
                                        <thead class="table-dark">
                                            <tr>
                                                <th>Mes</th>
                                                <th>Total</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="month in listSalesMonth">
                                                <td>{{ month[0] }}</td>
                                                <td align="right">{{ formatNumber(month[1]) }}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                <div class="col">
                                    <Bar id="my-chart-id" :options="chartOptions" :data="chartDataMonths" />
                                </div>
                            </div>

                        </div>
                    </div>
                </div>

            </div>
            <div class="row">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <div class="card-title">Ventas Por Mesero</div>
                            <div class="row">
                                <div class="col">
                                    <table class="table table-sm table-bordered">
                                        <thead class="table-dark">
                                            <tr>
                                                <th>Mesero</th>
                                                <th>Total</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="waiter in listSalesWaiter">
                                                <td>{{ waiter[0] }}</td>
                                                <td align="right">{{ formatNumber(waiter[1]) }}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                <div class="col">
                                    <Bar :data="chartDataWaiter" :options="chartOptions" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <div class="card-title">Ventas Por Mesas</div>
                            <Bar :data="chartDataWaiter" :options="chartOptions" />
                        </div>
                    </div>
                </div>
            </div>

        </div>
        <div class="col">
            <div class="row">
                <div class="col">
                    <table class="table table-sm table-bordered caption-top">
                        <caption>Ventas por Dia</caption>
                        <thead class="table-dark">
                            <tr>
                                <th scope="col">Fecha</th>
                                <th scope="col" class="text-center">Total</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-if="listSalesByDay.length === 0">
                                <td colspan="2" align="center">No hay datos</td>
                            </tr>
                            <tr v-for="sale in listSalesByDay">
                                <td>{{ sale[0] }}</td>
                                <td align="right">{{ formatNumber(sale[1]) }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="col">
                    <table class="table table-sm table-bordered caption-top">
                        <caption>Ventas por mesas</caption>
                        <thead class="table-dark">
                            <tr>
                                <th scope="col">Mesa</th>
                                <th scope="col" class="text-center">Total</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-if="listSalesByTable.length === 0">
                                <td colspan="2" align="center">No hay datos</td>
                            </tr>
                            <tr v-for="sale in listSalesByTable">
                                <td>{{ sale[0] }}</td>
                                <td align="right">{{ formatNumber(sale[1]) }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import { onBeforeMount, ref } from 'vue'
import { Bar, Pie } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement } from 'chart.js'
import { formatNumber } from '../../tools/utils'

const loading = ref(false)
const loadingSync = ref(false)
const title = ref('')
const total = ref(0)
const average = ref(0.0)
const averageWeek = ref(0.0)
const backgroundColor = ['#41B883', '#E46651', '#00D8FF', '#DD1B16'];

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement)

const chartDataCategory = ref([])
const chartDataProduct = ref([])
const chartDataProductUnits = ref([])
const chartDataCashier = ref([])
const chartDataWaiter = ref([])
const chartDataTable = ref([])
const listSalesCategory = ref([])
const listSalesProduct = ref([])
const listSalesProductUnits = ref([])
const listSalesMonth = ref([])
const listSalesWaiter = ref([])
const listSalesByDay = ref([])
const listSalesByTable = ref([])
const chartDataMonths = ref([])

const chartOptions = {
    responsive: true
}

const syncData = () => {
    loadingSync.value = true;
    let url = `${process.env.API_URL}/sync-remote-data`
    fetch(url).then(resp => resp.json()).then(resp => {
        loadingSync.value = false;
    })
}

onBeforeMount(() => {
    loading.value = true;
    let url = `${process.env.API_URL}/report`
    fetch(url)
        .then(resp => resp.json())
        .then(data => {
            let { sales_by_day, sales_by_category, sales_by_product, total_sales,
                sales_by_product_unit, sales_by_waiter, sales_by_table, average_by_day, sales_by_week, sales_by_month } = data

            title.value = `${sales_by_day[0][0]} al ${sales_by_day[sales_by_day.length - 1][0]}`

            listSalesProduct.value = sales_by_product
            listSalesCategory.value = sales_by_category
            listSalesMonth.value = sales_by_month
            listSalesWaiter.value = sales_by_waiter
            listSalesProductUnits.value = sales_by_product_unit

            chartDataCategory.value = {
                labels: sales_by_category.map(d => d[0]),
                datasets: [
                    {
                        backgroundColor,
                        label: "Ventas por Categorias",
                        data: sales_by_category.map(d => d[1])
                    }
                ]
            }
            total.value = total_sales
            average.value = average_by_day
            listSalesByDay.value = sales_by_day
            listSalesByTable.value = sales_by_table

            averageWeek.value = total_sales / sales_by_week.length

            chartDataProduct.value = {
                labels: sales_by_product.map(d => d[0]),
                datasets: [
                    {
                        backgroundColor,
                        label: "Ventas por Productos",
                        data: sales_by_product.map(d => d[1])
                    }
                ]
            }

            chartDataProductUnits.value = {
                labels: sales_by_product_unit.map(d => d[0]),
                datasets: [
                    {
                        backgroundColor,
                        label: "Ventas por Productos unidades",
                        data: sales_by_product_unit.map(d => d[1])
                    }
                ]
            }
            chartDataWaiter.value = {
                labels: sales_by_waiter.map(d => d[0]),
                datasets: [
                    {
                        backgroundColor,
                        label: "Ventas por Mesero",
                        data: sales_by_waiter.map(d => d[1])
                    }
                ]
            }

            chartDataMonths.value = {
                labels: sales_by_month.map(d => d[0]),
                datasets: [
                    {
                        backgroundColor,
                        label: "Ventas por Meses",
                        data: sales_by_month.map(d => d[1])
                    }
                ]
            }

            loading.value = false;
        })
})
</script>
<style></style>