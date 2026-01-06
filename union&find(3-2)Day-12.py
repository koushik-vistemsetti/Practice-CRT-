'''

def union_(self, a, b, par, rank1):
    pa = self.find(a, par)
    pb = self.find(b, par)
    if pa == pb:
        return
    if rank1[pa] < rank1[pb]:
        par[pa] = pb
    elif rank1[pa] > rank1[pb]:
        par[pb] = pa
    else:
        par[pb] = pa
        rank1[pa] += 1
def isConnected(self, x, y, par, rank1):
    return self.find(x, par) == self.find(y, par)
def find(self, x, par):
    if par[x] != x:
        par[x] = self.find(par[x], par)
    return par[x]
'''
'''

def krushkals_algorithm(adj):
    parent = [i for i in range(len(adj))]
    rank = [0]*len(adj)

    def find(n):
        if parent[n] != n:
            parent[n] = find(parent[n])
        return parent[n]

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra != rb:
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

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
print(krushkals_algorithm(d))

'''

'''
def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        parent[ra] = rb
        size[rb] += size[ra]
    else:
        parent[rb] = ra
        size[ra] += size[rb]
    return True


v, e = int(input()), int(input())
edges = [list(map(int, input().split())) for _ in range(e)]
parent = [i for i in range(v)]
size = [1]*v
req = 0
for n, m in edges:
    if not union(n, m):
        req += 1

roots = set(find(i) for i in range(len(parent)))
num_components = len(roots)

if req >= num_components - 1:
    print("can connect all components")
else:
    print("cannot connect all components")
'''


# all pair shortest path
'''
def apsp(graph):
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph    
m = int(input())
li = [list(map(int, input().split())) for _ in range(m)]
print(apsp(li))
'''


n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]

for via in range(0, n):
    for i, j, w in l:
        l[i*n+j][2] = min(l[i*n+via][2]+l[via*n+j][2], l[i*n+j][2])
print(l)
