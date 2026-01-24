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


### timeout 처리 로직 구현
# import asyncio

# async def f():
#     for i in range(1, 6):
#         r = i
#         if i & 1:
#             t = 1
#         else:
#             t = 5
#         try:
#             await asyncio.wait_for(asyncio.sleep(t), 2)
#         except asyncio.TimeoutError:
#             r = "실패"
#         yield r

# async def main():
#     async for res in f():
#         print(res)

# asyncio.run(main())

### 배치 처리 로직 구현
# import asyncio

# async def chunk(size):
#     buffer = []
#     for i in range(1, 11):
#         await asyncio.sleep(0.3)
#         buffer.append(i)
#         if len(buffer) == size:
#             yield buffer
#             buffer = []
#     if buffer:
#         yield buffer
    

# async def main():
#     async for batch in chunk(2):
#         print(batch)
# asyncio.run(main())