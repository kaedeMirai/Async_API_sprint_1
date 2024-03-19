from fastapi import APIRouter, Depends, HTTPException

from models.genre import Genre
from services.genre_service import GenreService, get_genre_service
from exceptions.exceptions import BadParamException
from dto.query_params_dto import QueryParamsDTO

router = APIRouter()


@router.get(
    '',
    response_model=list[Genre] | list,
    summary='Retrieve genres based on query',
    description='Retrieve all genres if query not specified or genres list filtered based on specified query'
)
async def multiple_genres(
        query_dto: QueryParamsDTO = Depends(),
        genre_service: GenreService = Depends(get_genre_service)):
    try:
        genres = await genre_service.retrieve_multiple(query_dto)
        return genres
    except BadParamException:
        raise HTTPException(status_code=422, detail='Bad request parameter specified, please check.')


@router.get(
    '/{genre_id}',
    response_model=Genre | dict,
    summary='Retrieve genre by Id',
    description='Retrieve all genre details based on specified genre Id'
)
async def genre_details(
        genre_id: str,
        genre_service: GenreService = Depends(get_genre_service)):
    genre = await genre_service.retrieve_by_id(genre_id)

    return genre
