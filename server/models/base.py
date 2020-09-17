# I Love China

__Author__ = 'Seenming'


from aiopg.sa import create_engine
from sqlalchemy.sql import insert, select, and_
from sqlalchemy import column
# from server.settings import DB_NAME, DB_USER, DB_PWD, DB_HOST
DB_USER = "postgres"
DB_PWD = "postgres"
DB_NAME = "qa_community"
DB_HOST = "127.0.0.1"


class BaseMixin:
    _engine = None
    conn = None

    @classmethod
    async def reconnect(cls):
        if not cls._engine:
            cls._engine = await create_engine(user=DB_USER, database=DB_NAME, host=DB_HOST, password=DB_PWD)

    @classmethod
    async def acquire_conn(cls):
        if not cls._engine:
            await cls.reconnect()
        cls.conn = await cls._engine.acquire()

    @classmethod
    async def insert_data(cls, **kwargs):
        if not cls.conn:
            await cls.acquire_conn()
        await cls.conn.execute(insert(cls.__table__).values(**kwargs))
    
    @classmethod
    async def fetch_one(cls, **kwargs):
        if not cls.conn:
            await cls.acquire_conn()
        condition = [column(key).__eq__(kwargs[key]) for key in kwargs]
        data = await (await cls.conn.execute(select(cls.__table__.c).where(and_(*tuple(condition))))).first()
        return data

    @classmethod
    async def fetch_many(cls):
        if not cls.conn:
            await cls.acquire_conn()
        return await cls.conn.execute(select(cls.__table__.c))

    @classmethod
    async def release_conn(cls):
        if not cls._engine:
            await cls.reconnect()
        if cls.conn:
            await cls._engine.release(cls.conn)
