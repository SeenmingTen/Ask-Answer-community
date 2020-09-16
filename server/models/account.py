# I Love China

__Author__ = 'Seenming'


import asyncio
from server.settings import DB_NAME, DB_USER, DB_PWD
from aiopg.sa import create_engine
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from server.models.base import BaseMixin


engine = create_engine(user=DB_USER, database=DB_NAME, host="127.0.0.1", password=DB_PWD)


Base = declarative_base()


class Account(Base, BaseMixin):
    
    __tablename__ = "account_info"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    password = Column(String(100))
    # create_date = Column(Date)
    # update_time = Column(DateTime)

    def __str__(self):
        return f"{self.username}"
    
    @classmethod
    async def insert_data(cls, **kwargs):
        if not cls.conn:
            await cls.acquire_conn()
        await cls.conn.execute(cls.__table__.insert().values(**kwargs))

    # @classmethod
    # async def create_table(cls):
    #     if not cls.conn:
    #         await cls.acquire_conn()
    #     print(cls.conn)
    #     await cls.conn.execute("""CREATE TABLE account_info(
    #                                 id serial primary key ,
    #                                 username varchar (30),
    #                                 password varchar (100))""")


if __name__ == '__main__':
    import time
    start_time = time.time()
    BaseMixin.acquire_conn()
    loop = asyncio.get_event_loop()
    tasks = [Account.insert_data(**{"username": f"user{i}", "password": "1234"}) for i in range(5)]
    task = asyncio.gather(*tasks)
    loop.run_until_complete(task)
    # for t in task:
    #     print(t.result())
    print(f"cost_time {time.time() - start_time}")

