# ##dict-missing test
# class MissingDict(dict):
#     def __missing__(self, key):
#         value = 1
#         self[key] = value
#         return value
    
# testdict = MissingDict()
# testdict[1] = 2
# print(testdict[2])
# print(testdict)

# ##comprehension test
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat = [x for row in matrix for x in row]
# print(flat)


##generator test - sum과 for루프가 각각 __iter__를 사용해서 다른 generator 객체 생성
# def normalize(numbers):
#     total = sum(numbers)
#     result = []
#     for value in numbers:
#         percent = 100 * value / total
#         result.append(percent)
#     return result

# class ReadVisits:
#     def __init__(self, line):
#         self.line = line
        
#     def __iter__(self):
#         for visitors in line:
#             yield int(visitors)

# line = [100,200,100,300,300]
# visits = ReadVisits(line)
# percentages = normalize(visits)
# print(percentages)
# assert sum(percentages) == 100.0         

##yield from test
def g1():
    for i in range(1,4):
        yield i

def g2():
    yield from [1,2,3]

a = g1()
print(next(a))
print(next(a))
print(next(a))
b = g2()
print(next(b))
print(next(b))
print(next(b))
