# Read graph from user in materix
'''
m = int(input())
li = [[int(input()) for _ in range(m)] for _ in range(m)]
print(li)
d = {}
for i in range(m):
    for j in range(m):
        if li[i][j] == 1:
            if i in d.keys():
                d[i].append(j)
            else:
                d[i] = [j]
print(d)
'''
# Print Nodes of graph using BFS using queue
#time complexity O(V+E)
#space complexity O(V)
m=int(input())
li=[[int(input()) for _ in range(m)] for _ in range(m)]
print(li)
d={}
visited=[False]*m
for i in range(m):
    for j in range(m):
        if li[i][j]==1:
            if i in d.keys():
                d[i].append(j)
            else:
                d[i]=[j]
print(d)
visited[0]=True
q=[0]
while len(q)!=0:
    t=q.pop(0)
    print(t,end=" ")
    for i in d[t]:
        if not visited[i]:
            visited[i]=True
            q.append(i)
#'''
# Print Nodes of graph using DFS using recursion
#time complexity O(V+E)
#space complexity O(V)
'''
def dfs(s):
    print(s,end=" ")
    visited[s]=True
    for i in d[s]:
        if not visited[i]:
            dfs(i)
m=int(input())
li=[[int(input()) for _ in range(m)] for _ in range(m)]
print(li)
d={}
for i in range(m):
    for j in range(m):
        if li[i][j]==1:
            if i in d.keys():
                d[i].append(j)
            else:
                d[i]=[j]
print(d)
visited=[False]*m
dfs(0)
#'''
# Print Nodes of graph using DFS using stack
'''
m=int(input())
li=[[int(input()) for _ in range(m)] for _ in range(m)]
print(li)
d={}
for i in range(m):
    for j in range(m):
        if li[i][j]==1:
            if i in d.keys():
                d[i].append(j)
            else:
                d[i]=[j]
print(d)
visited=[False]*m
s=[0]
while len(s)!=0:
    t=s.pop()
    print(t,end=" ")
    visited[t]=True
    for i in d[t]:
        if not visited[i]:
            s.append(i)
#'''
# Detect Cycle in graph using BFS by appending visited nodes in queue along with thier parent node
'''
m=int(input())
li=[[int(input()) for _ in range(m)] for _ in range(m)]
print(li)
d={}
for i in range(m):
    for j in range(m):
        if li[i][j]==1:
            if i in d.keys():
                d[i].append(j)
            else:
                d[i]=[j]
print(d)
visited=[False]*m
q=[(0,-1)]
while len(q)!=0:
    t=q.pop(0)
    if visited[t[0]]:
        print("Cycle Detected")
        break
    visited[t[0]]=True
    for i in d[t[0]]:
        if i!=t[1]:
            q.append((i,t[0]))
#'''

# Topological Sort using BFS
'''
def topological_sort_bfs(g):
    ino=[0]*len(g)
    for i in range(len(g)):
        for j in g[i]:
            ino[j]+=1
    for i in range(len(g)):
        for j in g[i]:
            ino[j]+=1
    q=[i for i in range(len(g)) if ino[i]==0]
    l=[]
    while q:
        t=q.pop(0)
        l.append(t)
        for i in g[t]:
            ino[i]-=1
            if ino[i]==0:
                q.append(i)
    return l

def topological_sort_dfs(g):
    v=[False]*len(g)
    l=[]
    for i in range(len(g)):
        if not v[i]:
            dfs(i,l,g,v)
    return l
def dfs(i,l,g,v):
        v[i]=True
        for j in g[i]:
            if not v[j]:
                dfs(j)
        l.append(i)

m=int(input())
l=[[map(int,input().split())] for _ in range(m)]
d={}
for i in range(m):
    for j in range(m):
        if l[i][j]==1:
            if i in d.keys():
                d[i].append(j)
            else:
                d[i]=[j]
print(topological_sort_bfs(d))
print(topological_sort_dfs(d))
#'''

# Detect Cycle using topological sort
'''
def detect_cycle(g):
    ino=[0]*len(g)
    for i in range(len(g)):
        for j in g[i]:
            ino[j]+=1
    for i in range(len(g)):
        for j in g[i]:
            ino[j]+=1
    q=[i for i in range(len(g)) if ino[i]==0]
    while q:
        t=q.pop(0)
        for i in g[t]:
            ino[i]-=1
            if ino[i]==0:
                q.append(i)
    return True

m=int(input())
l=[[map(int,input().split())] for _ in range(m)]
d={}
for i in range(m):
    for j in range(m):
        if l[i][j]==1:
            if i in d.keys():
                d[i].append(j)
            else:
                d[i]=[j]
print(detect_cycle(d))
#'''
# Schedule a timetable using topological sort or check whether graph is acyclic or not
'''
def schedule(g):
    ino=[0]*len(g)
    v=[False]*len(g)
    detect=False
    for i in range(len(g)):
        for j in g[i]:
            ino[j]+=1
    q=[i for i in range(len(g)) if ino[i]==0]
    while q:
        t=q.pop(0)
        v[t]=True
        for i in g[t]:
            if v[i]:
                detect=True
                break
            ino[i]-=1
            if ino[i]==0:
                q.append(i)
    if detect:
        print('Found cycle')
    else:
        print('No cycle')
        print('Schedule:',q)
    
m=int(input('Enter number of subjects:'))
l=[0][0]*m
while True:
    t=input()
    if t=='n':
        break
    a,b=map(int,t.split())
    l[a][b]=1
d={}
for i in range(m):
    d[i]=[]
    for j in range(m):
        if l[i][j]==1:
            d[i].append(j)
print(d)
print(schedule(d))
#'''
# Shortest path using BFS
'''
def shortest_path(g,s):
    d=[]
    for i in range(len(g)):
        d[i]=float('inf')
    d[s]=0
    q=[(0,s)]
    while q:
        wt,n=q.pop(0)
        for i in g[n]:
            if d[i]>d[n]+1:
                d[i]=d[n]+1
                q.append((d[i],i))
    return d
m=int(input())
l=[[map(int,input().split())] for _ in range(m)]
adj={}
for i in range(m):
    for j in range(m):
        if l[i][j]==1:
            if i in adj.keys():
                adj[i].append(j)
            else:
                adj[i]=[j]
print(shortest_path(adj,0))
#'''
'''

def shortest_path(g,s):
    d=[float('inf')]*len(g)
    d[s]=0
    q=[(0, s)]
    while q:
        wt,n=q.pop(0)
        if wt>d[n]:
            continue
        for v,w in g.get(n,[]):
            if d[v]>d[n]+w:
                d[v]=d[n]+w
                q.append((d[v],v))
    return d
m=int(input())
l=[[map(int,input().split())] for _ in range(m)]
adj={}
for i in range(m):
    for j in range(m):
        if l[i][j]>0:
            if i in adj.keys():
                adj[i].append((j,1))
            else:
                adj[i]=[(j,1)]
print(shortest_path(adj,0))
'''
