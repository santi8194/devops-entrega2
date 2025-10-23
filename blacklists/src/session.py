import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SessionConfig:
    def __init__(self): ...

    def url(self):
        db_user = "postgres"
        db_pass = "postgres"
        db_host = "blacklist-postgres.cxi4kauewdcn.us-east-2.rds.amazonaws.com"
        db_port = 5432
        db_name = "db_blacklist"
        return f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"


session_config = SessionConfig()
engine = create_engine(session_config.url())
Session = sessionmaker(bind=engine)
