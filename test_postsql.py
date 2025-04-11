import asyncpg
import asyncio

async def test_conn():
    conn = await asyncpg.connect(user='surajkumar', password='Surajkumar',
                                 database='url_database', host='127.0.0.1')
    print("✅ Connected successfully!")
    await conn.close()

asyncio.run(test_conn())
