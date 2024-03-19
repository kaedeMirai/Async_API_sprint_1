from fastapi import APIRouter, Depends, HTTPException

from models.film import Film
from services.film_service import FilmService, get_film_service
from exceptions.exceptions import BadParamException
from dto.query_params_dto import QueryParamsDTO

router = APIRouter()


@router.get(
    '',
    response_model=list[Film] | list,
    summary='Retrieve films based on query',
    description='Retrieve all films if query not specified or films list filtered based on specified query'
)
async def multiple_films(
        query_dto: QueryParamsDTO = Depends(QueryParamsDTO),
        film_service: FilmService = Depends(get_film_service)):
    try:
        films = await film_service.retrieve_multiple(query_dto)
        return films
    except BadParamException:
        raise HTTPException(status_code=422, detail='Bad request parameter specified, please check.')


@router.get(
    '/{film_id}',
    response_model=Film | dict,
    summary='Retrieve film by Id',
    description='Retrieve all film details based on specified film Id'
)
async def film_details(
        film_id: str,
        film_service: FilmService = Depends(get_film_service)):
    film = await film_service.retrieve_by_id(film_id)

    return film
