import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

import Components from "unplugin-vue-components/vite";
import { ElementPlusResolver } from "unplugin-vue-components/resolvers";
import {resolve} from "pathe";

export default defineConfig({
    resolve: {
        alias: {
            '@': resolve(__dirname, `src`)
        }
    },
    server: {
        host: "127.0.0.1",
        port: 3000, //vite项目启动时自定义端口
        open: true, //vite项目启动时自动打开浏览器
    },


    plugins: [
        vue(),
        Components({
        resolvers: [ElementPlusResolver()],
        }),


    ],



})
