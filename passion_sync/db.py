from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from passion_sync.settings import settings
from sqlalchemy.orm import sessionmaker


class Base(DeclarativeBase):
    pass


db_url = settings.database_url if not settings.test_db else settings.test_database_url
engine = create_engine(db_url, echo=settings.echo_sql)

Base.metadata.create_all(engine)

Session = sessionmaker(engine)


def get_session():
    session = Session()
    return session
