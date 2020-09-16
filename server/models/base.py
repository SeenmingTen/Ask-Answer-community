# I Love China

__Author__ = 'Seenming'


from server.settings import DB_NAME, DB_USER, DB_PWD
from aiopg.sa import create_engine


class BaseMixin:
    _engine = None
    conn = None

    @classmethod
    async def reconnect(cls):
        if not cls._engine:
            cls._engine = await create_engine(user=DB_USER, database=DB_NAME, host="127.0.0.1", password=DB_PWD)

    @classmethod
    async def acquire_conn(cls):
        if not cls._engine:
            await cls.reconnect()
        print(cls._engine)
        cls.conn = await cls._engine.acquire()
        print(cls.conn)

    @classmethod
    async def release_conn(cls):
        if not cls._engine:
            await cls.reconnect()
        if cls.conn:
            await cls._engine.release(cls.conn)
