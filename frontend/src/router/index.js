import {createRouter} from  "vue-router";
import {createWebHistory} from "vue-router";


// 这些都会传递给 `createRouter`
const routes = [
    // 动态字段以冒号开始
    { path: '/', component: ()=>import("@/views/MovieList.vue") },
    { path: '/home', redirect: "/" },
    { path: '/login', component: ()=>import("@/views/Login.vue") },
    { path: '/settings', component: ()=>import("@/views/Settings.vue") },
    { path: '/edit/:id',props:true, component: ()=>import("@/views/Edit.vue") },

    // 将匹配所有内容并将其放在 `$route.params.pathMatch` 下
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: ()=>import("@/views/NotFound.vue") },
]


const router = createRouter({
    history:createWebHistory(),
    routes
})


router.beforeEach((to, from) => {
    // ...
    // 返回 false 以取消导航
    return false
})
export default router