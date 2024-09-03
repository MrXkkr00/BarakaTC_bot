from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool


from data import config


class Database_User:

    def __init__(self) -> None:
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def disconnect(self):
        await self.pool.close()

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            user_id varchar(255),
            BTK_id varchar(255),
            name varchar(255),
            nomer varchar(255),
            qosh_nomer varchar(255),
            viloyat varchar(255),
            address varchar(255),
            vaqt varchar(255)
            );
"""
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, user_id: str = None, BTK_id: str = None, name: str = None, nomer: str = None,
                       qosh_nomer: str = None, viloyat: str = None,  address: str = None,  vaqt: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(user_id, BTK_id,  name, nomer, qosh_nomer, viloyat, address, vaqt) 
        VALUES($1, $2, $3, $4, $5, $6, $7, $8) returning *
        """
        return await self.execute(sql, user_id, BTK_id,  name, nomer, qosh_nomer, viloyat, address,vaqt, fetchrow=True)

    # async def update_user_bonus(self, viloyat, bonus):
    #     # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
    #
    #     sql = f"""
    #     UPDATE Users SET bonus=$1 WHERE viloyat=$2
    #     """
    #     return await self.execute(sql, bonus, viloyat, fetchrow=True)

    async def update_user_btk(self, id, BTK_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET BTK_id=$1 WHERE id=$2
        """
        return await self.execute(sql, BTK_id, id,  fetchrow=True)


    async def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        return await self.execute("SELECT COUNT(*) FROM Users", fetchval=True)

    # async def delete_user(self, address, oy, day, soat):
    #     await self.execute("DELETE FROM Users WHERE address=$1 AND oy = $2 AND day=$3 AND soat =$4 ", address, oy, day,
    #                        soat, execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)


