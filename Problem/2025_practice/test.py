import heapq

a = []
b = heapq.nlargest(1,a)
print(b[-1])