from fastapi import APIRouter

movie = APIRouter(tags=['电影相关'])


@movie.get("/movie",summary="电影列表")
async def movies_list():
    return "movies_list"



@movie.post("/movie",summary="新增电影")
async def add_movie():
    return "add_movie"



@movie.put("/movie",summary="编辑电影")
async def update_movie():
    return "update_movie"


@movie.delete("/movie",summary="删除电影")
async def del_movie():
    return "del_movie"