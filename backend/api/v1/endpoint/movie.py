from typing import List

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError

from backend.core.deps import get_current_user
from backend.models import Movie
from backend.schemas import Movie_Pydantic, MovieIn_Pydantic

movie = APIRouter(tags=['电影相关'],dependencies=[Depends(get_current_user)])


class Status(BaseModel):
    message: str


@movie.get("/movie", summary="电影列表", response_model=List[Movie_Pydantic])
async def movies_list(limit: int = 10, page: int = 1):
    #  limit 是显示的条数 ，page是页数

    skip = (page - 1) * limit
    # select * from movie limit offset,limit
    # select * from movie limit 0,10
    return await Movie_Pydantic.from_queryset(Movie.all().offset(skip).limit(limit))


@movie.post("/movie", summary="新增电影", response_model=Movie_Pydantic)
async def add_movie(movie: MovieIn_Pydantic):
    movie_obj = await Movie.create(**movie.dict(exclude_unset=True))
    # movie_obj = await Movie.create(name="",year="",xx="")
    return await Movie_Pydantic.from_tortoise_orm(movie_obj)


@movie.put("/movie/{movie_id}", summary="编辑电影", responses={404: {"model": HTTPNotFoundError}})
async def update_movie(movie_id: int, movie: MovieIn_Pydantic):
    updated_count = await Movie.filter(id=movie_id).update(**movie.dict(exclude_unset=True))
    if not updated_count:
        raise HTTPException(status_code=404, detail=f"Movie {movie_id} not found")
    return await Movie_Pydantic.from_queryset_single(Movie.get(id=movie_id))


@movie.get("/movie/{movie_id}", summary="查找电影", response_model=Movie_Pydantic,
           responses={404: {"model": HTTPNotFoundError}})
async def get_user(movie_id: int):
    return await Movie_Pydantic.from_queryset_single(Movie.get(id=movie_id))


@movie.delete("/movie/{movie_id}", summary="删除电影", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def del_movie(movie_id: int):
    deleted_count = await Movie.filter(id=movie_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Movie {movie_id} not found")
    return Status(message=f"Deleted Movie {movie_id}")
