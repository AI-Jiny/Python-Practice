import dis
# def gen():
#     yield 1
#     yield 2

# dis.dis(gen)


async def foo():
    await 1

dis.dis(foo)