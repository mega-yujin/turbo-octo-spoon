from app.system.database import engine
from src.app.system.database import Base
from app.system.schemas import (
    UsersTable,
    PizzasTable,
    CategoriesTable,
    IngredientsTable,
    OrdersTable,
    pizza_ingredient_table,
    orders_pizzas_table,
)

TABLES = [
    PizzasTable.__table__,
    IngredientsTable.__table__,
    UsersTable.__table__,
    CategoriesTable.__table__,
    OrdersTable.__table__,
]
Base.metadata.create_all(engine, tables=TABLES)

pizza_ingredient_table.create(engine)
orders_pizzas_table.create(engine)
