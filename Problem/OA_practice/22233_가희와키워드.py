import sys
input = sys.stdin.readline

N, M = map(int, input().split())
notepad = {input().rstrip() for _ in range(N)}
posts = []
ans = []
for _ in range(M):
    words = input().rstrip().split(',')
    for word in words:
        if word in notepad:
            notepad.remove(word)
            
    ans.append(len(notepad))

for an in ans:
    print(an)