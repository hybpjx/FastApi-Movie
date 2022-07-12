<script setup>

import {ref} from "vue"
import Header from "./Header.vue";
import Footer from "./Footer.vue";

const isLogin = ref(false) // 默认未登录


</script>



<template xmlns="http://www.w3.org/1999/html">

  <div class="common-layout">
    <el-container>
      <h2>
        <img src="@/assets/images/avatar.png" alt="" style="width: 40px">
        WatchList(fastapi)
      </h2>

      <el-header>

        <Header />
      </el-header>

      <el-main>
        <router-view></router-view>
      </el-main>



      <el-footer>
        <img src="@/assets/images/totoro.gif" class="dudu" alt=""/>

        <Footer />

      </el-footer>
    </el-container>

  </div>
</template>



<style scoped>
.el-header{
  height: 32px;
  background-color: black;
  line-height: 32px;
  text-align: center;
  padding: 0 !important;
}

.el-main {
  padding: 0 3px 0 3px !important;
}

.el-footer {
  color: #888;
  margin-top: 15px;
  text-align: center;
  padding: 10px;
}

.dudu {
  display: block;
  margin: 0 auto;
  height: 100px;
}

</style>