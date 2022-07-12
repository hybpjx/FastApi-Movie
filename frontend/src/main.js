import { createApp } from 'vue'
import App from './App.vue'
import "normalize.css"
import "@/assets/css/style.css"

import router from "./router";


createApp(App).use(router).mount('#app')
