from datetime import datetime, timedelta
from typing import Optional
from uuid import uuid4

from fastapi import Depends, HTTPException, status

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.auth.models import UserInDB, User, Token, UserCreate
from app.pizzeria.models import Pizza, PizzaCategory, Ingredient
from app.config import AppSettings, get_settings
from app.system.database import get_db_session
from app.system.schemas import UsersTable, PizzasTable, IngredientsTable, CategoriesTable


class PizzeriaService:
    def __init__(
            self,
            db_session: Session = Depends(get_db_session),
            settings: AppSettings = Depends(get_settings),
    ):
        self.db_session = db_session
        self.settings = settings

    def get_pizza(self, name: str):
        pass

    def get_all_pizzas(self) -> list[Pizza]:
        all_pizzas = self.db_session.query(PizzasTable).all()
        return [Pizza.from_orm(pizza) for pizza in all_pizzas]

    def add_pizza(self, pizza: Pizza):
        ingredients = [self._get_ingredient(ingredient.name) for ingredient in pizza.ingredients]
        pass

    def _get_ingredient(self, name: str):
        db_ingredient = self.db_session.query(IngredientsTable).filter(IngredientsTable.name == name).first()
        return db_ingredient
