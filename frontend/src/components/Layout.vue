<template xmlns="http://www.w3.org/1999/html">

  <div class="common-layout">
    <el-container>
      <h2>
        <img src="@/assets/images/avatar.png" alt="" style="width: 40px">
        WatchList(fastapi)
      </h2>

    <Header />
      <Header></Header>


      <p>
        8 TOTAL
      </p>

      <el-main>
        <ul class="movie-list">
          <li v-for="i in 8">
            Dead Poets Society-1991

            <span class="float-right">

              <template v-if="!IsLogin">
                <el-button size="small">edit</el-button>
                <el-button size="small">delete</el-button>
              </template>

              <a class="imdb" href="https://www.imdb.com/find?q=Dead Poets Society" target="_blank">IMDB</a>
            </span>
          </li>
        </ul>

      </el-main>

      <img src="@/assets/images/totoro.gif" class="dudu" alt=""/>

      <el-footer>

         <span>© 2021
        <a href="#">
          HelloFlask
        </a>
         </span>
        <p>
          <a>
            使用FastAPI + Vue3 翻抄 HelloFlask一书中的项目
          </a>
        </p>
      </el-footer>
    </el-container>

  </div>
</template>


<script>
export default {
  name: "Layout",
  components:"Header"
}

import Header from "./Header.vue";

import {ref} from "vue"

const IsLogin = ref(false) // 默认未登录


</script>

<style scoped>

.el-footer {
  color: #888;
  margin-top: 15px;
  text-align: center;
  padding: 10px;
}

.el-main {
  padding: 0 3px 0 3px !important;
}

.movie-list {
  list-style-type: none;
  padding: 0;
  margin-bottom: 10px;
  box-shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);
}

.movie-list li {
  padding: 12px 24px;
  border-bottom: 1px solid #ddd;
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

.dudu {
  display: block;
  margin: 0 auto;
  height: 100px;
}

.el-button {
  font-size: 12px !important;
  padding: 3px 5px !important;
  text-decoration: none !important;
  cursor: pointer !important;
  background-color: white !important;
  color: black !important;
  border: 1px solid #555555 !important;
  border-radius: 5px !important;
}

</style>