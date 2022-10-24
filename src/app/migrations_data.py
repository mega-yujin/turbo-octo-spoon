import datetime
from uuid import UUID

from sqlalchemy import insert
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


def add_pizzas_to_order(pizzas: list[Pizza], order: Order):
    prepared_data = [{'order_id': order.id, 'pizza_id': pizza.id} for pizza in pizzas]
    print(prepared_data)
    conn = engine.connect()
    conn.execute(orders_pizzas_table.insert(), prepared_data)


def test_add_pizzas_to_order(db: DBSession):
    prepared_data = [
        {
            'order_id': UUID('aac80f79-b7ca-4399-b1c2-814910d85049'),
            'pizza_id': UUID('aa79d86f-6e4e-49dd-ab04-afa9022f76df')
        },
        {
            'order_id': UUID('bbc80f79-b7ca-4399-b1c2-814910d85049'),
            'pizza_id': UUID('bb79d86f-6e4e-49dd-ab04-afa9022f76df')
        },
    ]

    # db.add(orders_pizzas_table.insert(prepared_data))
    # db.execute(orders_pizzas_table.insert(), prepared_data)
    # db.commit()

    # conn = engine.connect()
    # conn.execute(orders_pizzas_table.insert(), prepared_data)


# ss = DBSession()
# test_add_pizzas_to_order(ss)

USERS = [
    User(
        username='finik',
        email='kot@mail.com',
        is_active=True,
    ),
    User(
        username='papa',
        email='papa@mail.com',
        is_active=True,
    )
]

INGREDIENTS = [
    Ingredient(
        name='cheese',
    ),
    Ingredient(
        name='tomato',
    ),
    Ingredient(
        name='mozarella',
    )
]

PIZZAS = [
    Pizza(
        id=UUID('c479d86f-6e4e-49dd-ab04-afa9022f76df'),
        name='margherita',
        category=PizzaCategory(id=UUID('0d92cad1-5c9b-4ad9-b617-eb46380df8a7'), name='classic'),
        description='mega pizza',
        price=20.5,
        calories=520,
        weight=320,
        ingredients=[
            Ingredient(
                name='mozarella',
            ),
            Ingredient(
                name='tomatoto',
            ),
        ],
    )
]

ORDERS = [
    Order(
        # user=USERS[0],
        id=UUID('1fc80f79-b7ca-4399-b1c2-814910d85049'),
        user_id=UUID('68cf2205-b6f9-4a7a-bb66-fe3115302c10'),
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
        name='classic',
    ),
    PizzaCategory(
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

# pizza_ingredient_table.create(engine)
# orders_pizzas_table.create(engine)

### INSERT DATA INTO DATABASE ###

db_session = DBSession()

# for user in USERS:
#     create_user(db_session, user)

# for ing in INGREDIENTS:
#     add_ingredients(db_session, ing)

# for pizza in PIZZAS:
#     add_pizzas(db_session, pizza)

# for order in ORDERS:
#     add_order(db_session, order)

# add_pizzas_to_order(PIZZAS, ORDERS[0])

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

# order = db_session.query(OrdersTable).first()
# item = order.ordered_items
# print(item)
#
# ass = db_session.query(orders_pizzas_table).first()
# print(ass)
