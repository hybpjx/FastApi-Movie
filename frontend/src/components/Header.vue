<script>

// 拿到目前所有项目的路由
const router = useRouter()
export default {

  name: "Footer",
  data(){
    return {
      currentRouter:router.getRoutes()
    }
  }
}

defineProps({
  isLogin:{
    type:Boolean,
    default:false
  }
})

// 任意点击 即可触发的事件
const handleSelect=()=>{
  console.log(123)
}


</script>

<template>


  <el-menu :default-active="1" mode="horizontal" @select="handleSelect">
    <template v-for="router in currentRouter"></template>
    <el-menu-item index="1">Home</el-menu-item>
    <template v-if="!isLogin">
      <el-menu-item index="2">Login</el-menu-item>
    </template>
    <template v-else>
      <el-menu-item index="2">LogOut</el-menu-item>
      <el-menu-item index="3">settings</el-menu-item>
    </template>


  </el-menu>


</template>



<style scoped>

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