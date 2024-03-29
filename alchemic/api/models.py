from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Ingredient(BaseModel):
    """Ingredient model."""

    model_config = ConfigDict(from_attributes=True)

    pk: int
    name: str


class IngredientPayload(BaseModel):
    """Ingredient payload model."""

    name: str = Field(min_length=2, max_length=127)


class Potion(BaseModel):
    """Potion model."""

    model_config = ConfigDict(from_attributes=True)

    pk: int
    name: str
    ingredients: list[Ingredient]
    description: Optional[str | None] = Field(max_length=150, default=None)


class PotionPayload(BaseModel):
    """Potion payload model."""

    name: str = Field(min_length=1, max_length=127)
    ingredients: list[int] = Field(min_length=1)
    description: Optional[str | None] = Field(max_length=150, default=None)
