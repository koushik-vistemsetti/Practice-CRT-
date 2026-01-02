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
