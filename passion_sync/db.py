from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from passion_sync.settings import settings
from sqlalchemy.orm import sessionmaker

class Base(DeclarativeBase):
    pass

engine = create_engine(settings.test_database_url, echo=settings.echo_sql)

Base.metadata.create_all(engine)

Session = sessionmaker(engine)

def get_session():
    session = Session()
    return session