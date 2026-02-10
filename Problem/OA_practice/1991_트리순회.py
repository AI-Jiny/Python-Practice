N = int(input())
input_tree = [[x for x in input().split()] for _ in range(N)]
tree = {}
for t in input_tree:
    p, c1, c2 = t
    tree[p] = [c1, c2]

        

def preorder(p):
    print(p, end="")
    for c in tree[p]:
        if c != '.':
            preorder(c) 

def inorder(p):
    c1, c2 = tree[p]

    if c1 != '.':
        inorder(c1)
    
    print(p, end="")
    
    if c2 != '.':
        inorder(c2)

def postorder(p):
    for c in tree[p]:
        if c != '.':
            postorder(c) 
    print(p, end="")


preorder('A')
print()
inorder('A')
print()
postorder('A')