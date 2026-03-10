from collections import deque
'''
for x in range(-1, 2):
    for y in range(-1, 2):
        if x != 0 or y != 0:
            print(x, y)

print(*[(i, j) for i in range(-1, 2)
      for j in range(-1, 2) if not (i == 0 and j == 0)])


def connected_islands_bfs(m):
    if not m:
        return 0

    r = len(m)
    c = len(m[0])
    visited = [0]*r
    for i in range(r):
        visited[i] = [0]*c
    count = 0
    rows = [-1, -1, -1, 0, 0, 1, 1, 1]
    cols = [-1, 0, 1, -1, 1, -1, 0, 1]
    q = []

    for i in range(r):
        for j in range(c):
            if m[i][j] == 1 and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = 1
                while q:
                    c1, c2 = q.pop(0)
                    for k in range(len(rows)):
                        n1 = c1+rows[k]
                        n2 = c2+cols[k]
                        if (n1 >= 0 and n1 < r) and (n2 >= 0 and n2 < c) and m[n1][n2] == 1 and not visited[n1][n2]:
                            visited[n1][n2] = 1
                            q.append((n1, n2))
                count += 1
    return count


r = int(input())
m = []
for i in range(r):
    l = list(map(int, input().split()))
    m.append(l)
print(connected_islands_bfs(m))

def rotting_oranges(m):
    if not m:
        return -1
    r = len(m)
    c = len(m[0])
    fresh = 0
    q = []
    for i in range(r):
        for j in range(c):
            if m[i][j] == 2:
                q.append((i, j, 0))
            elif m[i][j] == 1:
                fresh += 1
    time = 0
    rows = [-1, 0, 1, 0]
    cols = [0, -1, 0, 1]
    while q:
        c1, c2, t = q.pop(0)
        time = max(time, t)
        for k in range(4):
            n1 = c1+rows[k]
            n2 = c2+cols[k]
            if (n1 >= 0 and n1 < r) and (n2 >= 0 and n2 < c) and m[n1][n2] == 1:
                fresh -= 1
                m[n1][n2] = 2
                q.append((n1, n2, t+1))
    if fresh == 0:
        return time
    return -1
'''

'''
def prims_algorithm(adj):
    visited = [0]*len(adj)
    path = []  # [(n,w)]
    queue = [(0, 0, -1)]  # w,n,p
    c = 0
    while queue:
        queue.sort()
        w, n, p = queue.pop(0)
        if visited[n]:
            continue
        visited[n] = 1
        if p != -1:
            path.append((p, n, w))
        for v, wt in adj.get(n, []):
            if not visited[v]:
                queue.append((wt, v, n))
        c += w
    return path, c


m = int(input())
li = [[int(input()) for _ in range(m)] for _ in range(m)]
print(li)
d = {}
for i in range(m):
    for j in range(m):
        if li[i][j] > 0:
            if i in d.keys():
                d[i].append((j, li[i][j]))
            else:
                d[i] = [(j, li[i][j])]
print(d)
print(prims_algorithm(d))

'''