#array of edges (directed) [start, end]
n = 8
A = [[0,1],[1, 2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]

print(A)

#convert array of edges -> adjacency matrix
M = []
for i in range(n):
    M.append([0] * n)

for u, v in A:
    M[u][v] = 1
    #if undirected uncomment following line
    M[v][u] = 1

for row in M:
    print(' '.join(str(x) for x in row))

#convert array of edges into adjacency list
from collections import defaultdict
D = defaultdict(list)

for u, v in A:
    D[u].append(v)
    #for undirected graph uncomment the following line
    #D[v].append(u)

print(D)
print(D[3])

#dfs with recursion Time: O(v+e) where v is nodes and e is edges
def dfs_recursive(node):
    print(node) #processing
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)

source = 0
seen = set()
seen.add(source)
dfs_recursive(source)
print()


#iterative DFS with stack - Time: O(V + E)
source2 = 0
seen2 = set()
seen2.add(source2)
stack = [source2]
while stack:
    node = stack.pop()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen2:
            seen2.add(nei_node)
            stack.append(nei_node)


print()
# BFS with a queue - O(V + E)
source3 = 0
from collections import deque
seen3 = set()
seen3.add(source3)
q = deque()
q.append(source3)


while q:
    node = q.popleft()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen3:
            seen3.add(nei_node)
            q.append(nei_node)


