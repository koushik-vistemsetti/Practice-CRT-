from collections import deque


def krushkals_algorithm(adj):
    parent = [i for i in range(len(adj))]
    rank = [0]*len(adj)

    def find(n):
        if parent[n] != n:
            parent[n] = find(parent[n])
        return parent[n]

    def union(a, b):
        up1 = find(a)
        up2 = find(b)
        if up1 != up2:
            if rank[up1] < rank[up2]:
                parent[up1] = up2
            elif rank[up1] > rank[up2]:
                parent[up2] = up1
            else:
                parent[up2] = up1
                rank[up1] += 1

    edges = []
    for u in adj:
        for v, w in adj[u]:
            edges.append((w, u, v))
    edges.sort()
    mst = []
    cost = 0
    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
            cost += w
    return mst, cost


m = int(input())
li = [list(map(int, input().split())) for _ in range(m)]
d = {}
for i in range(m):
    for j in range(m):
        if li[i][j] > 0:
            if i in d.keys():
                d[i].append((j, li[i][j]))
            else:
                d[i] = [(j, li[i][j])]
print(krushkals_algorithm(d))
'''
# 2nd Question


def shortest_path(m):
    r = len(m)
    c = len(m[0])
    queue = deque()
    visited = [[0]*c for _ in range(r)]
    s = 0

    for i in range(r):
        for j in range(c):
            if m[i][j] == 2:
                queue.append((i, j, 0))
                visited[i][j] = 1

    while queue:
        i, j, s = queue.popleft()
        for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = x+i, y+j
            if ni < 0 or ni == r or nj < 0 or nj == c:
                continue
            if m[ni][nj] == 0 or visited[ni][nj] == 1:
                continue
            if m[ni][nj] == 3:
                print("Path found, cost=", s+1)
                return
            visited[ni][nj] = 1
            queue.append((ni, nj, s+1))
    print("Path Does Not Exist")
    return


m = int(input())
li = [list(map(int, input().split())) for _ in range(m)]
shortest_path(li)
'''

# 3rd question
'''

def cycle_detection(d, m):
    visited = [0]*m
    q = [(0, -1)]
    while len(q) != 0:
        t = q.pop(0)
        if visited[t[0]] == 1:
            print("Cycle Detected")
            break
        visited[t[0]] = 1
        for i in d[t[0]]:
            if i != t[1]:
                q.append((i, t[0]))
    else:
        print("No Cycle Detected")

m = int(input())
li = [list(map(int, input().split())) for _ in range(m)]
d = {}
for i in range(m):
    for j in range(m):
        if li[i][j] == 1:
            if i in d.keys():
                d[i].append(j)
            else:
                d[i] = [j]
cycle_detection(d, m)
'''
