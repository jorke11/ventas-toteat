import 'bootstrap/dist/css/bootstrap.css'
import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './routes/index'

createApp(App).use(router).mount('#app')

import 'bootstrap/dist/js/bootstrap.js'