import asyncio

counter = 0

async def inc():
    global counter
    temp = counter
    counter = temp + 1
    await asyncio.sleep(0)  # 여기서 다른 코루틴으로 양보

async def main():
    await asyncio.gather(*(inc() for _ in range(1000)))

asyncio.run(main())
print(counter)