from fastapi import APIRouter, Depends, HTTPException

from models.person import Person
from services.person_service import PersonService, get_person_service
from exceptions.exceptions import BadParamException
from dto.query_params_dto import QueryParamsDTO

router = APIRouter()


@router.get(
    '',
    response_model=list[Person] | list,
    summary='Retrieve persons based on query',
    description='Retrieve all persons if query not specified or persons list filtered based on specified query'
)
async def multiple_persons(
        query_dto: QueryParamsDTO = Depends(),
        person_service: PersonService = Depends(get_person_service)):
    try:
        persons = await person_service.retrieve_multiple(query_dto)
        return persons
    except BadParamException:
        raise HTTPException(status_code=422, detail='Bad request parameter specified, please check.')


@router.get(
    '/{person_id}',
    response_model=Person | dict,
    summary='Retrieve person by Id',
    description='Retrieve all person details based on specified person Id'
)
async def person_details(
        person_id: str,
        person_service: PersonService = Depends(get_person_service)):
    person = await person_service.retrieve_by_id(person_id)

    return person
