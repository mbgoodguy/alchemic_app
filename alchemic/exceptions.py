from fastapi import HTTPException
from starlette import status


class CustomException(HTTPException):

    @staticmethod
    def non_existent_potion():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Potion does not exist",
        )

    @staticmethod
    def non_existent_ingredient():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingredient does not exist",
        )

