<template>
  <ul class="movie-list">
    <p>
      8 TOTAL
    </p>
    <li v-for="i in 8">
      Dead Poets Society-1991

      <span class="float-right">

              <template v-if="!isLogin">
                <el-button size="small">edit</el-button>
                <el-button size="small">delete</el-button>
              </template>

              <a class="imdb" href="https://www.imdb.com/find?q=Dead Poets Society" target="_blank">IMDB</a>
            </span>
    </li>
  </ul>
</template>

<script setup>

</script>

<style scoped>

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