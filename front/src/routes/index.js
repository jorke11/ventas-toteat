import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/home/home_page.vue';
import InvoicePage from '../pages/invoice/invoice_page.vue';
import CategoryPage from '../pages/category/category_page.vue';
import WaiterPage from '../pages/waiter/waiter_page.vue';
import CashierPage from '../pages/cashier/cashier_page.vue';
import ProductPage from '../pages/product/product_page.vue';

const routes = [
    {
        path: "/",
        name: "Home",
        component: HomePage
    },
    {
        path: "/invoice",
        name: "Invoice",
        component: InvoicePage
    },
    {
        path: "/category",
        name: "Categorias",
        component: CategoryPage
    },
    {
        path: "/waiter",
        name: "Meseros",
        component: WaiterPage
    },
    {
        path: "/cashier",
        name: "Cajeros",
        component: CashierPage
    },
    {
        path: "/product",
        name: "Productos",
        component: ProductPage
    },

]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
});

export default router;