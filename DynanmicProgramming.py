# def fac(n):
#     if n < 1:
#         return 0
#     if n == 1:
#         return 1
#     return n*fac(n-1)


# def fib1(n, dp):
#     dp = [-1]*(n+2)
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if dp[n] != -1:
#         return dp[n]
#     dp[n] = fib1(n-1, dp)+fib1(n-2, dp)
#     return dp[n]


# def fib(n):
#     c = 0
#     p = 0
#     p1 = 1
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     for i in range(n-2):
#         c = p+p1
#         p = p1
#         p1 = c
#     return c


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# def nth_prime(n):
#     count = 0
#     num = 2
#     while True:
#         if is_prime(num):
#             count += 1
#             if count == n:
#                 return num
#         num += 1


# n = int(input())
# dp = [-1]*(n+2)
# s = 0
# f, p = 0, 0
# while n:
#     a = n % 10
#     f += fib(a)
#     p += nth_prime(a)
#     s = s+fac(a)
#     n = n//10
# print(s, f, p)

# def stairs(n):
#     if n == 0 or n == 1:
#         return 1
#     return stairs(n-1)+stairs(n-2)


# print(stairs(int(input())))
'''
def knapsack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n-1] <= W:
        return max(val[n-1] + knapsack(W - wt[n-1], wt, val, n-1), knapsack(W, wt, val, n-1))
    else:
        return knapsack(W, wt, val, n-1)


W = int(input("Enter knapsack capacity: "))
n = int(input("Enter number of items: "))
wt = list(map(int, input("Enter weights: ").split()))
val = list(map(int, input("Enter profits: ").split()))
print("Maximum profit:", knapsack(W, wt, val, n))

'''

# fractional knopsack
'''

def fractionalKnapsack(W, wt, val, n):
    z = list(zip([val[i]/wt[i] for i in range(n)], wt, val))
    z.sort(reverse=True)
    total = 0.0
    for r, wt, value in z:
        if W == 0:
            break
        if wt <= W:
            total += value
            W -= wt
        else:
            total += value * (W / wt)
            W = 0
            break
    return total


w = int(input())
n = int(input())
wt = list(map(int, input().split()))
val = list(map(int, input().split()))

print(fractionalKnapsack(w, wt, val, n))

'''
# o/1 knapsack
'''

n=int(input())
li=list(list(map(int,input().split())) for _ in range(n))
li.sort(key=lambda x:x[1],reverse=True)
cap=int(input())
s,i=0,0
while i<len(li) and cap>0:
    if cap>=li[i][1]:
        cap-=li[i][1]
        s+=li[i][0]
    i+=1
print(s)
'''
#
'''
def knapsack_re(c, it, p):
    if c <= 0 or it >= len(p):
        return 0
    if p[it][1] > c:
        return knapsack_re(c, it+1, p)
    return max(p[it][0] + knapsack_re(c - p[it][1], it+1, p), knapsack_re(c, it+1, p))


n = int(input())
p = list(list(map(int, input().split())) for _ in range(n))
c = int(input())
print(knapsack_re(c, 0, p))

'''
# knapsack tabulation
'''

def knapsack_tab(W, wt, val, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1]
                               [w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
            print(dp[i][w], end=" ")
        print()
    return dp[n][W]


W = int(input("Enter knapsack capacity: "))
n = int(input("Enter number of items: "))
wt = list(map(int, input("Enter weights: ").split()))
val = list(map(int, input("Enter profits: ").split()))
print("Maximum profit:", knapsack_tab(W, wt, val, n))
'''
# q

# time
'''

def sum(li, n, dp):
    if n >= len(li):
        return 0
    if dp[n] != -1:
        return dp[n]
    inc = li[n]+sum(li, n+2, dp)
    exl = sum(li, n+1, dp)
    dp[n] = max(inc, exl)
    return dp[n]
'''

# li = list(map(int, input().split()))
# dp = [-1]*len(li)
# print(sum(li, 0, dp))
# print(dp)
# c, p1, p2 = 0, li[0], 0
# time complexity o(n) space o(1)
'''
for i in range(1, len(li)):
    c = max(p1, p2+li[i])
    p2 = p1
    p1 = c
print(p1)
'''
# for n in range(5, -1, -1):
#     l = li[n]
#     if (n+2 <= len(li)-1):
#         l += dp[n+2]
#     r = 0
#     if (n+1 <= len(li)-1):
#         r += dp[n+1]
#     dp[n] = max(l, r)
# print(dp)


# using dp memoization
'''
def check(li, tar, dp, n):
    if tar == 0:
        return True
    if n >= len(li):
        return False
    if dp[tar] != -1:
        return dp[tar]
    inc = False
    if tar >= li[n]:
        inc = check(li, tar-li[n], dp, n+1)
    exl = check(li, tar, dp, n+1)
    dp[tar] = inc or exl
    return dp[tar]


li = list(map(int, input().split()))
tar = int(input())
dp = [-1]*(tar+1)
print(check(li, tar, dp, 0), dp)
'''
# def check_tab(li, tar):
#     dp = [[False for _ in range(tar+1)] for _ in range(len(li)+1)]
#     for i in range(len(li)+1):
#         dp[i][0] = True
#     for i in range(1, len(li)+1):
#         for j in range(1, tar+1):
#             if li[i-1] <= j:
#                 dp[i][j] = dp[i-1][j-li[i-1]] or dp[i-1][j]
#             else:
#                 dp[i][j] = dp[i-1][j]
#     return dp[len(li)][tar]

# check if there are subset with sum equal to half of total sum
'''
def check_re(li,n,tar):
    if tar==0:
        return True
    if n>=len(li):
        return False
    inc=False
    if tar>=li[n]:
        inc=check_re(li,n+1,tar-li[n])
    exl=check_re(li,n+1,tar)
    return inc or exl

li = list(map(int, input().split()))
tar=sum(li)
if tar%2==0:
    print(check_re(li, 0, tar//2))
else:
    print(False)
    '''
# check how many ways we can achive target sum


def check_re(li, n, tar):
    if tar == 0:
        return True
    if n >= len(li):
        return False
    inc = False
    if tar >= li[n]:
        inc = check_re(li, n+1, tar-li[n])
    exl = check_re(li, n+1, tar)
    return inc + exl


li = list(map(int, input().split()))
tar = int(input())
print(check_re(li, 0, tar))

# using dp memoization


def check(li, tar, dp, n):
    if tar == 0:
        return 1
    if n >= len(li):
        return 0
    if dp[n][tar] != -1:
        return dp[n][tar]
    inc = 0
    if tar >= li[n]:
        inc = check(li, tar-li[n], dp, n+1)
    exl = check(li, tar, dp, n+1)
    dp[n][tar] = inc + exl
    return dp[-1][-1]


li = list(map(int, input().split()))
tar = int(input())
dp = [[-1 for _ in range(tar+1)] for _ in range(len(li)+1)]
print(check(li, tar, dp, 0))


#
