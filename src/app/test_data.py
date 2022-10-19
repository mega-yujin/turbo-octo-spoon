from app.system.database import SessionLocal
from app.auth import models
from app.system.database import engine
from app.system.db_tables import pizza_ingredient_table, Ingredient, Pizza, User
from src.app.system.database import Base


### TESTDATA ###


def create_user(db: SessionLocal, user: models.User):
    password = 'ololo'
    db_user = User(
        id=user.id,
        username='fffinik',
        email=user.email,
        hashed_password=password,
        is_active=user.is_active,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


py_user = models.User(
    id='857cbf13-d22a-4d1c-91ff-b74de2d916d8',
    username='finik',
    email='kot@mail.com',
    is_active=True,
)

### TABLES CREATION ###

tables = [Pizza.__table__, Ingredient.__table__, ]
Base.metadata.create_all(engine, tables=tables)

pizza_ingredient_table.create(engine)

### INSERT DATA INTO DATABASE ###

db_session = SessionLocal()
new_user = create_user(db_session, py_user)
print(new_user)
