import asyncio

class A:
    def __await__(self):
        yield 1
        return 123

async def f():
    res = await A()
    print(res)
    return 1

asyncio.run(f())