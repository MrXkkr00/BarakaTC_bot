import asyncio

from utils.db_api.trek_nomer_sql import Database_Trek_nomer


async def test():
    db = Database_Trek_nomer()
    await db.create()
    user = await db.select_all_users()
    # user = await db.add_user(user_id="5325425", BTK_id="31", trek_nomer="trek_nomer")
    print(user)


asyncio.run(test())
