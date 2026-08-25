class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

#===============================
# Recursive Traversals Time: O(n), Space O(n)
#===============================
def pre_order(root):
    if not root:
        return
    print(root)
    pre_order(root.left)
    pre_order(root.right)

pre_order(A)
print()
def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root)
    in_order(root.right)

in_order(A)

def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root)

print()
post_order(A)

#===============================
# Iterative Traversals, Time: O(n), Space O(n)
#===============================
def iterative_pre(node):
    stack = [node]
    while stack:
        node = stack.pop()
        print(node)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)

print()
iterative_pre(A)

# Level order traversal BFS, Time: O(n), Space O(n)
from collections import deque
def level_order(node):
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
        print(node)

print()
level_order(A)

#Check if value exists DFS Time: O(n), Space O(n)
def search(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    return search(node.left, target) or search(node.right, target)

print()
print(search(A, 20))


# Binary Search Trees
A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

print()
print(A2)

print()
in_order(A2)

print()

# search BST in log(n)
def search_bst(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    if target < node.val: return search_bst(node.left, target)
    else: return search_bst(node.right, target)

print(search_bst(A2, 20))