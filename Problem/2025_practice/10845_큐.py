from collections import deque

class MyDeque(deque):
    def push(self, n):
        self.append(n)
        

    def pop(self):
        if len(self) == 0:
            return -1
        return super().popleft()

    def size(self):
        return len(self)

    def empty(self):
        is_empty = 0 if len(self) else 1
        return is_empty

    def front(self):
        front_num = self[0] if len(self) else -1
        return front_num

    def back(self):
        back_num = self[-1] if len(self) else -1
        return back_num
    
N = int(input())
list_command = [[command, *num] for command, *num in (input().split() for _ in range(N))]
dq = MyDeque()

for command, *num in list_command:
    method = getattr(dq, command)
    if (res := method(*num)) is not None:
        print(res)
