import datetime

from app.system.database import DBSession
from app.auth.models import User
from app.orders.models import Order, UserWithOrders
from app.pizzeria.models import Pizza, PizzaCategory, Ingredient
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


### TESTDATA ###


def create_user(db: DBSession, user: User):
    password = 'ololo'
    db_user = UsersTable(
        id=user.id,
        username=user.username,
        email=user.email,
        hashed_password=password,
        is_active=user.is_active,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def add_ingredients(db: DBSession, ingredient: Ingredient):
    db_category = IngredientsTable(**ingredient.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def add_category(db: DBSession, p_category: PizzaCategory):
    db_category = CategoriesTable(**p_category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def add_pizzas(db: DBSession, pizza: Pizza):
    db_pizza = PizzasTable(
        id=pizza.id,
        name=pizza.name,
        category_id=pizza.category.id,
        description=pizza.description,
        price=pizza.price,
        calories=pizza.calories,
        weight=pizza.weight,
        ingredients=[IngredientsTable(**ingredient.dict()) for ingredient in pizza.ingredients],
    )
    db.add(db_pizza)
    db.commit()
    db.refresh(db_pizza)
    return db_pizza


def add_order(db: DBSession, order: Order):
    db_order = OrdersTable(
        id=order.id,
        user_id=order.user_id,
        city=order.city,
        street=order.street,
        building=order.building,
        delivery_time=order.delivery_time,
        total_price=order.total_price,
        is_delivered=order.is_delivered,
        ordered_items=[PizzasTable(
            id=item.id,
            name=item.name,
            category_id=item.category.id,
            description=item.description,
            price=item.price,
            calories=item.calories,
            weight=item.weight,
            ingredients=[IngredientsTable(**ingredient.dict()) for ingredient in item.ingredients],
        ) for item in order.ordered_items],
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


USERS = [
    User(
        id='857cbf13-d22a-4d1c-91ff-b74de2d916d8',
        username='finik',
        email='kot@mail.com',
        is_active=True,
    ),
    User(
        id='317cbf13-d22a-4d1c-91ff-b74de2d916d8',
        username='papa',
        email='papa@mail.com',
        is_active=True,
    )
]

INGREDIENTS = [
    Ingredient(
        id='857cbf13-d22a-4d1c-91ff-b74de2d916d2',
        name='cheese',
    ),
    Ingredient(
        id='561cbf13-d22a-4d1c-91ff-b74de21916d2',
        name='tomato',
    ),
    Ingredient(
        id='857cbf13-4fg2-4d1c-91ff-d74de2d916d2',
        name='mozarella',
    )
]

PIZZAS = [
    Pizza(
        id='857cbf13-4fg2-4d1c-91ff-b64d82d9112g',
        name='margherita',
        category=PizzaCategory(id='1', name='classic'),
        description='mega pizza',
        price=20.5,
        calories=520,
        weight=320,
        ingredients=[
            Ingredient(
                id='857cbf13-4fg2-4d1f-91fl-b74de2d916d2',
                name='mozarella',
            ),
            Ingredient(
                id='561cbf13-d23a-4d1c-91f0-b74de2d916d2',
                name='tomatoto',
            ),
        ],
    )
]

ORDERS = [
    Order(
        id='1',
        # user=USERS[0],
        user_id='USERS[0]',
        city='Minsk',
        street='Some street',
        building='2342',
        delivery_time=datetime.datetime.now(),
        total_price=100500,
        is_delivered=False,
        ordered_items=PIZZAS
    )
]

CATEGORIES = [
    PizzaCategory(
        id=1,
        name='classic',
    ),
    PizzaCategory(
        id=2,
        name='not classic',
    ),
]

### TABLES CREATION ###

tables = [
    PizzasTable.__table__,
    IngredientsTable.__table__,
    UsersTable.__table__,
    CategoriesTable.__table__,
    OrdersTable.__table__
]
Base.metadata.create_all(engine, tables=tables)

pizza_ingredient_table.create(engine)
orders_pizzas_table.create(engine)

### INSERT DATA INTO DATABASE ###

db_session = DBSession()

# for user in USERS:
#     create_user(db_session, user)

# for ing in INGREDIENTS:
#     add_ingredients(db_session, ing)
#
# for pizza in PIZZAS:
#     add_pizzas(db_session, pizza)

# for order in ORDERS:
#     add_order(db_session, order)

# for category in CATEGORIES:
#     add_category(db_session, category)

# all_pizzas = db_session.query(PizzasTable).all()
# pizza = all_pizzas[0]
#
# all_users = db_session.query(UsersTable).all()
# user = all_users[0]

# orders = user.orders
# print(orders[0].__dict__)

# print(UserWithOrders(**user.__dict__, orders=user.orders).json())
# print(Pizza(**pizza.__dict__, ingredients=pizza.ingredients, category=pizza.category).json())
