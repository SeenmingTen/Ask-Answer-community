# I Love China

__Author__ = 'Seenming'

import asyncio
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from models.base import BaseMixin


Base = declarative_base()


class Account(Base, BaseMixin):
    
    __tablename__ = "account_info"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(10), nullable=False, index=True)
    password = Column(String(50), default="", nullable=False)
    create_time = Column(DateTime, default=datetime.now())
    update_time = Column(DateTime, onupdate=datetime.now(), default=datetime.now())

    def __str__(self):
        return f"{self.username}"

    # @classmethod
    # async def create_table(cls):
    #     if not cls.conn:
    #         await cls.acquire_conn()
    #     print(cls.conn)
    #     await cls.conn.execute("""CREATE TABLE account_info (
    #                                 id SERIAL NOT NULL,
    #                                 username VARCHAR(10) NOT NULL,
    #                                 password VARCHAR(50) NOT NULL,
    #                                 create_time TIMESTAMP WITHOUT TIME ZONE,
    #                                 update_time TIMESTAMP WITHOUT TIME ZONE,
    #                                 PRIMARY KEY (id)
    #                             )""")


if __name__ == '__main__':
    import time
    start_time = time.time()
    # from sqlalchemy.engine import create_engine
    # from server.settings import DB_NAME, DB_USER, DB_PWD
    # engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PWD}@127.0.0.1:5432/{DB_NAME}", echo=True)
    # Base.metadata.create_all(engine)
    loop = asyncio.get_event_loop()
    # tasks = [Account.insert_data(**{"username": f"user{i}", "password": "1234"}) for i in range(5)]
    # task = asyncio.gather(*tasks)
    task = asyncio.ensure_future(Account.fetch_one(**{"username": "admin", "password":'123456'}))
    loop.run_until_complete(task)
    print(task.result())
    # for t in task:
    #     print(t.result())
    print(f"cost_time {time.time() - start_time}")

