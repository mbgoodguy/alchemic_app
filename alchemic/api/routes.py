from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from alchemic.api import models
from alchemic.database import models as db_models
from alchemic.database.session import get_db_session
from exceptions import CustomException

router = APIRouter(prefix="/v1", tags=["Alchemist app"])


@router.post("/ingredients", status_code=status.HTTP_201_CREATED)
async def create_ingredient(
        data: models.IngredientPayload,
        session: AsyncSession = Depends(get_db_session),
) -> models.Ingredient:
    ingredient = db_models.Ingredient(**data.model_dump())
    session.add(ingredient)
    await session.commit()
    await session.refresh(ingredient)
    return models.Ingredient.model_validate(ingredient)


@router.get("/ingredients", status_code=status.HTTP_200_OK)
async def get_ingredients(
        session: AsyncSession = Depends(get_db_session),
) -> list[models.Ingredient]:
    ingredients = await session.scalars(select(db_models.Ingredient))
    return [models.Ingredient.model_validate(ingredient) for ingredient in ingredients]


@router.get("/ingredients/{pk}", status_code=status.HTTP_200_OK)
async def get_ingredient(
        pk: int,
        session: AsyncSession = Depends(get_db_session),
) -> models.Ingredient:
    ingredient = await session.get(db_models.Ingredient, pk)
    if ingredient is None:
        CustomException.non_existent_ingredient()
    return models.Ingredient.model_validate(ingredient)


@router.post("/potions", status_code=status.HTTP_201_CREATED)
async def create_potion(
        data: models.PotionPayload,
        session: AsyncSession = Depends(get_db_session),
) -> models.Potion:
    data_dict = data.model_dump()
    ingredients = await session.scalars(
        select(db_models.Ingredient).where(
            db_models.Ingredient.pk.in_(data_dict.pop("ingredients"))
        )
    )
    potion = db_models.Potion(**data_dict, ingredients=list(ingredients))
    session.add(potion)
    await session.commit()
    await session.refresh(potion)
    return models.Potion.model_validate(potion)


@router.get("/potions", status_code=status.HTTP_200_OK)
async def get_potions(
        session: AsyncSession = Depends(get_db_session),
) -> list[models.Potion]:
    potions = await session.scalars(select(db_models.Potion))
    return [models.Potion.model_validate(potion) for potion in potions]


@router.get("/potions/{pk}", status_code=status.HTTP_200_OK)
async def get_potion(
        pk: int,
        session: AsyncSession = Depends(get_db_session),
) -> models.Potion:
    potion = await session.get(db_models.Potion, pk)
    if potion is None:
        CustomException.non_existent_potion()
    return models.Potion.model_validate(potion)


@router.put('/potions/{pk}')
async def update_potion(
        pk: int,
        potion_data: models.PotionPayload,
        session: AsyncSession = Depends(get_db_session)
) -> models.Potion:
    try:
        potion = await session.get(db_models.Potion, pk)
    except Exception as e:
        print(e)

    if potion is None:
        CustomException.non_existent_potion()

    # Получаем экземпляры Ingredient по их первичным ключам
    ingredients = await session.execute(select(db_models.Ingredient).filter(db_models.Ingredient.pk.in_(potion_data.ingredients)))
    ingredient_instances = [row for row in ingredients]
    # print(ingredient_instances)
    # for ingredient in ingredient_instances:
    #     print(ingredient[0])

    # Обновите атрибуты зелья, включая список ингредиентов
    potion.name = potion_data.name
    potion.description = potion_data.description
    potion.ingredients = [ingredient[0] for ingredient in ingredient_instances]

    await session.commit()
    await session.refresh(potion)

    return models.Potion.model_validate(potion)

