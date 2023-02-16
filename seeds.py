from app.models import User
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

## possible root of mysql error when running seeds.py in .env? (1045, "Access denied for user 'root'@'localhost' (using password: YES)")