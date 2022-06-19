<template>

  <div class="common-layout">
    <el-container>
      
      <h2>
        <img src="@/assets/images/avatar.png" alt="" style="width: 40px">
        WatchList(fastapi)
      </h2>
      <el-header>

      <el-menu
            :default-active="1"
            mode="horizontal"
            @select="$"
        >
          <el-menu-item index="1">Home</el-menu-item>
        <template v-if="!LogStatus">
          <el-menu-item index="2" >Login</el-menu-item>
        </template>
        <template v-else>
          <el-menu-item index="2">LogOut</el-menu-item>
          <el-menu-item index="2" v-if="LogStatus">settings</el-menu-item>

        </template>


        </el-menu>

      </el-header>

      <h2>8 TOTAL</h2>

      <el-main>Main</el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </div>
</template>



<script>
export default {
name: "Layout"
}
import {ref} from "vue"
const LogStatus= ref(true) // 默认未登录




</script>

<style scoped>
.el-footer {
  color: #888;
  margin-top: 15px;
  text-align: center;
  padding: 10px;
}
.el-header .el-menu {
  height: 32px;
  background-color: black;
  line-height: 32px;
  text-align: center;
  padding: 0 !important;
}

.el-main {
  padding: 0 3px 0 3px !important;
}

.imdb {
  font-size: 12px;
  font-weight: bold;
  color: black;
  text-decoration: none;
  background: #f5c518;
  border-radius: 5px;
  padding: 3px 5px;
}

.float-right {
  float: right;
}

.el-menu {
  height: 32px;
  background-color: black;
  line-height: 32px;
  text-align: center;
  padding: 0 !important;
}
.el-menu-item {
  height: 32px !important;
  color: white;
  padding: 8px 12px !important;
}
.el-menu {
  height: 32px;
  border: none !important;
}

</style>