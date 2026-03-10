# GFG COIN-CHANGE PROBLEM
'''
# recursive approach time complexity: O(2^n) space: O(n)

def count_re(c, m, n):
    if c == 0:
        return 1
    if c < 0 or n <= 0:
        return 0
    return count_re(c - m[n - 1], m, n) + count_re(c, m, n - 1)


# memonization with recursion time complexity: O(c*n) space: O(c*n)

def count_re_memo(c, m, n, dp):
    if c == 0:
        return 1
    if c < 0 or n <= 0:
        return 0
    if (c, n) in dp:
        return dp[(c, n)]
    dp[(c, n)] = count_re_memo(c - m[n - 1], m,
                               n, dp) + count_re_memo(c, m, n - 1, dp)
    return dp[(c, n)]

# DP APPROACH time complexity: O(c*n) space: O(n)


def count(m, n):
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    print(dp)
    for i in range(0, len(m)):
        for j in range(m[i], n + 1):
            dp[j] += dp[j - m[i]]
    return dp[n]


n = int(input())  # number of coins
m = list(map(int, input().split()))  # values of coins
c = int(input())  # total amount
print(count_re_memo(c, m, n, {}))
print(count_re(c, m, n))
print(count(m, c))
'''
# generate sub sequences
'''
def subsequence(s, curr, i):
    if i == len(s):
        print(curr)
        return
    subsequence(s, curr + s[i], i + 1)
    subsequence(s, curr, i + 1)

s = input()
subsequence(s, "", 0)
'''
# longest sub sequense
'''

def lcs(s1, s2, n, m):
    if n == 0 or m == 0:
        return 0
    if s1[n - 1] == s2[m - 1]:
        return 1 + lcs(s1, s2, n - 1, m - 1)
    else:
        return max(lcs(s1, s2, n - 1, m), lcs(s1, s2, n, m - 1))


def lcs_memo(s1, s2, n, m, dp):
    if n == 0 or m == 0:
        return 0
    if (n, m) in dp:
        return dp[(n, m)]
    if s1[n - 1] == s2[m - 1]:
        dp[(n, m)] = 1 + lcs_memo(s1, s2, n - 1, m - 1, dp)
        return dp[(n, m)]
    else:
        dp[(n, m)] = max(lcs_memo(s1, s2, n - 1, m, dp),
                         lcs_memo(s1, s2, n, m - 1, dp))
        return dp[(n, m)]




s1 = input()
s2 = input()
i=len(s1)
j=len(s2)

#using tabulation
dp1=[[0 for i in range(m+1)] for j in range(n+1)]
for k in range (1,i+1):
    for l in range (1,j+1):
        if s1[k-1]==s2[l-1]:
            dp1[k][l]=1+dp1[k-1][l-1]
        else:
            dp1[k][l]=max(dp1[k-1][l],dp1[k][l-1])
print(dp1[i][j])

dp=[-1]*( (i+1)*(j+1) )
print(lcs(s1, s2, len(s1), len(s2)))
print(lcs_memo(s1, s2, len(s1), len(s2),dp))
'''

# check palindrome
'''
def check_palindrone(s, i, j):
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
            continue
        return False
    return True if i >= j else False


s = input()
i = 0
j = len(s)-1
if check_palindrone(s, i, j):
    print("palindrone")
else:
    print("not palindrone")
'''

'''
def lpss(s, i, j):
    if i > j:
        return 0
    if i == j:
        return 1
    if s[i] == s[j]:
        return 2 + lpss(s, i + 1, j - 1)
    else:
        return max(lpss(s, i + 1, j), lpss(s, i, j - 1))


def lpss_memo(s, i, j, dp):
    if dp[i][j] != -1:
        return dp[i][j]
    if i > j:
        dp[i][j] = 0
    elif i == j:
        dp[i][j] = 1
    elif s[i] == s[j]:
        dp[i][j] = 2 + lpss_memo(s, i + 1, j - 1, dp)
    else:
        dp[i][j] = max(lpss_memo(s, i + 1, j, dp), lpss_memo(s, i, j - 1, dp))
    return dp[i][j]


def lpps_tabulation(s, dp1):
    n = len(s)
    dp1 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1, -1, -1):
        dp1[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp1[i][j] = 2 + dp1[i+1][j-1]
            else:
                dp1[i][j] = max(dp1[i+1][j], dp1[i][j-1])
    return dp1[0][n-1]


s = input()
i = 0
j = len(s)-1
dp = [-1]*len(s)*len(s)
dp1 = [-1]*len(s)*len(s)
print(lpss(s, i, j))
print(lpss_memo(s, i, j, [[-1 for _ in range(len(s))] for _ in range(len(s))]))
print(lpps_tabulation(s, dp1))
'''
# find the mminimum no of insertion and deletion to make PALINDROME using recursion

'''
def delete_palindrome(s, i, j):
    if i >= j:
        return 0
    if s[i] == s[j]:
        return delete_palindrome(s, i + 1, j - 1)
    else:
        return 1 + min(delete_palindrome(s, i + 1, j), delete_palindrome(s, i, j - 1))


def delete_palindrome_memo(s, i, j, dp):
    if i >= j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s[i] == s[j]:
        dp[i][j] = delete_palindrome_memo(s, i + 1, j - 1, dp)
    else:
        dp[i][j] = 1 + min(delete_palindrome_memo(s, i + 1, j, dp),
                           delete_palindrome_memo(s, i, j - 1, dp))
    return dp[i][j]


def delete_palindrome_tabulation(s):
    n = len(s)
    dp1 = [[0 for _ in range(n)] for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp1[i][j] = dp1[i + 1][j - 1]
            else:
                dp1[i][j] = 1 + min(dp1[i + 1][j], dp1[i][j - 1])
    return dp1[0][n - 1]


s = input()
i = 0
j = len(s)-1
print(delete_palindrome_memo(
    s, i, j, [[-1 for _ in range(len(s))] for _ in range(len(s))]))
print(delete_palindrome_tabulation(s))
print(delete_palindrome(s, i, j))
'''

# longest subsequence palindromic string using tabulation print even the subsequence

'''
def lsps_tabulation(s):
    n = len(s)
    dp1 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1, -1, -1):
        dp1[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp1[i][j] = 2+dp1[i+1][j-1]
            else:
                dp1[i][j] = max(dp1[i+1][j], dp1[i][j-1])
    lcs = ""
    i = 0
    j = n-1
    while i < j:
        if s[i] == s[j]:
            lcs = s[i] + lcs + s[j]
            i += 1
            j -= 1
        elif dp1[i+1][j] > dp1[i][j-1]:
            i += 1
        else:
            j -= 1
    print("Longest palindromic subsequence is",
          lcs, "and the length is", dp1[0][n-1])
    return lcs, dp1[0][n-1]


s = input()
print(lsps_tabulation(s))
'''

# find the smallest super sequence using recursion

'''
def ss(s1, s2, n, m):
    if n == 0:
        return m
    if m == 0:
        return n
    if s1[n - 1] == s2[m - 1]:
        return 1 + ss(s1, s2, n - 1, m - 1)
    else:
        return 1 + min(ss(s1, s2, n - 1, m), ss(s1, s2, n, m - 1))


def ss_print(s1, s2, n, m):
    if n == 0:
        return s2[:m]
    if m == 0:
        return s1[:n]
    if s1[n - 1] == s2[m - 1]:
        return ss_print(s1, s2, n - 1, m - 1) + s1[n - 1]
    return min(ss_print(s1, s2, n - 1, m) + s1[n - 1],
               ss_print(s1, s2, n, m - 1) + s2[m - 1], key=len)


def ss_memo(s1, s2, n, m, dp):
    if n == 0:
        return m
    if m == 0:
        return n
    if (n, m) in dp:
        return dp[(n, m)]
    if s1[n - 1] == s2[m - 1]:
        dp[(n, m)] = 1 + ss_memo(s1, s2, n - 1, m - 1, dp)
        return dp[(n, m)]
    else:
        dp[(n, m)] = 1 + min(ss_memo(s1, s2, n - 1, m, dp),
                             ss_memo(s1, s2, n, m - 1, dp))
        return dp[(n, m)]


def ss_tabulation(s1, s2):
    n = len(s1)
    m = len(s2)
    dp1 = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp1[i][j] = j
            elif j == 0:
                dp1[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp1[i][j] = 1 + dp1[i - 1][j - 1]
            else:
                dp1[i][j] = 1 + min(dp1[i - 1][j], dp1[i][j - 1])
    return dp1[n][m]


s1 = input()
s2 = input()
n = len(s1)
m = len(s2)
print(ss(s1, s2, n, m))
print(ss_print(s1, s2, len(s1), len(s2)))
print(ss_memo(s1, s2, n, m, {}))
print(ss_tabulation(s1, s2))

'''

# find how many times s2 occurs in s1 as a subsequence using recursion

'''
def count_subsequence(s1, s2, n, m, i=0, j=0):
    if j == m:
        return 1
    if i == n:
        return 0
    if s1[i] == s2[j]:
        return count_subsequence(s1, s2, n, m, i+1, j+1) + count_subsequence(s1, s2, n, m, i+1, j)
    else:
        return count_subsequence(s1, s2, n, m, i+1, j)


def count_subsequence_memo(s1, s2, n, m, dp):
    if m == 0:
        return 1
    if n == 0:
        return 0
    if dp[n][m] != -1:
        return dp[n][m]
    if s1[n - 1] == s2[m - 1]:
        dp[n][m] = count_subsequence_memo(
            s1, s2, n - 1, m - 1, dp) + count_subsequence_memo(s1, s2, n - 1, m, dp)
    else:
        dp[n][m] = count_subsequence_memo(s1, s2, n - 1, m, dp)
    return dp[n][m]


def count_subsequence_tabulation(s1, s2, n, m):
    dp1 = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp1[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp1[i][j] = dp1[i - 1][j - 1] + dp1[i - 1][j]
            else:
                dp1[i][j] = dp1[i - 1][j]
    return dp1[n][m]


s1 = input()
s2 = input()
n = len(s1)
m = len(s2)
dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
print(count_subsequence(s1, s2, n, m))
print(count_subsequence_memo(s1, s2, n, m, dp))
print(count_subsequence_tabulation(s1, s2, n, m))
'''
# edit distance

'''
def edit_distance(s1, s2, n, m):
    if n == 0:
        return m
    if m == 0:
        return n
    if s1[n - 1] == s2[m - 1]:
        return edit_distance(s1, s2, n - 1, m - 1)
    return 1 + min(edit_distance(s1, s2, n - 1, m),
                   edit_distance(s1, s2, n, m - 1),
                   edit_distance(s1, s2, n - 1, m - 1)
                   )

s1 = input()
s2 = input()
print(edit_distance(s1, s2, len(s1), len(s2)))
'''

# wild card matching

'''
def wild_card_matching(s1, s2, m, n):
    if n == 0 and m == 0:
        return True
    if m > 0 and n == 0:
        for i in range(m):
            if s2[i] != '*':
                return False
        return True
    if n > 0 and m == 0:
        return False
    if s2[m - 1] == '?' or s1[n - 1] == s2[m - 1]:
        return wild_card_matching(s1, s2, n - 1, m - 1)
    if s2[m - 1] == '*':
        return wild_card_matching(s1, s2, n - 1, m) or wild_card_matching(s1, s2, n, m - 1)
    return False


def wild_card_matching_memo(s1, s2, m, n, dp):
    if dp[m][n] != -1:
        return dp[m][n]
    if m == 0 and n == 0:
        dp[m][n] = True
    elif m > 0 and n == 0:
        for i in range(m):
            if s2[i] != '*':
                dp[m][n] = False
                return False
        dp[m][n] = True
    elif n > 0 and m == 0:
        dp[m][n] = False
    elif s2[m - 1] == '?' or s1[n - 1] == s2[m - 1]:
        dp[m][n] = wild_card_matching_memo(s1, s2, m - 1, n - 1, dp)
    elif s2[m - 1] == '*':
        dp[m][n] = wild_card_matching_memo(
            s1, s2, m, n - 1, dp) or wild_card_matching_memo(s1, s2, m - 1, n, dp)
    else:
        dp[m][n] = False
    return dp[m][n]


def wild_card_matching_tabulation(s1, s2):
    n = len(s1)
    m = len(s2)
    dp1 = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    dp1[0][0] = True
    for i in range(1, m + 1):
        if s2[i - 1] == '*':
            dp1[i][0] = dp1[i - 1][0]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s2[i - 1] == '?' or s1[j - 1] == s2[i - 1]:
                dp1[i][j] = dp1[i - 1][j - 1]
            elif s2[i - 1] == '*':
                dp1[i][j] = dp1[i - 1][j] or dp1[i][j - 1]
            else:
                dp1[i][j] = False
    return dp1[m][n]

s2 = input()
s1 = input()
print(wild_card_matching(s1, s2, len(s2), len(s1)))
print(wild_card_matching_memo(s1, s2, len(s2), len(s1), [
      [-1 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]))
print(wild_card_matching_tabulation(s1, s2))
'''

# longest increasing subsequence

'''
def lis(s, n):
    dp = [1] * n
    parent = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if s[i] > s[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = [j]
                elif dp[j] + 1 == dp[i]:
                    parent[i].append(j)
    max_len = max(dp)

    def build_paths(i):
        if not parent[i]:
            return [[s[i]]]
        paths = []
        for p in parent[i]:
            for seq in build_paths(p):
                paths.append(seq + [s[i]])
        return paths

    all_lis = []
    for i in range(n):
        if dp[i] == max_len:
            all_lis.extend(build_paths(i))

    return max_len, len(all_lis), all_lis


s = list(map(int, input().split()))
n = len(s)
print(lis(s, n))
'''

# generate all the permutaion for a string using recursion
'''


def permutaion(s, i, j):
    if i == j:
        print(''.join(s))
    else:
        for k in range(i, j+1):
            s[i], s[k] = s[k], s[i]
            permutaion(s, i+1, j)
            s[i], s[k] = s[k], s[i]


s = list(input())
permutaion(s, 0, len(s)-1)
'''
# s = input()


# def perm(op, ip):
#     if len(ip) == 1:
#         print(op+ip)
#         return
#     for i in range(len(ip)):
#         perm(op+ip[i], ip[:i]+ip[i+1:])


# perm("", s)

# find the minimum no of cuts to make a string palindrome using recursion

# def is_palindrome(s):
#     return s == s[::-1]
# space complexity O(n^2) time complexity O(2^n)
'''
def min_cuts(s):
    if s == s[::-1]:  # is_palindrome(s):
        return 0
    if len(s) == 1:
        return 0
    res = 999
    for i in range(1, len(s)):
        if s[i:] == s[i:][::-1]:  # is_palindrome(s[i:]):
            res = min(res, 1 + min_cuts(s[i:]))
    return res


print(min_cuts(s))
'''


# matrix grid souce to destination
# 1 total no of steps
'''

def fun(m, i, j):
    if i == len(m) - 1 and j == len(m[0]) - 1:
        return 1
    if i >= len(m) or j >= len(m[0]):
        return float('inf')
    return 1+min(fun(m, i+1, j), fun(m, i, j+1))


m = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(fun(m, 0, 0))


# 2 minimum path
def fun2(m, i, j):
    if i >= len(m) or j >= len(m[0]):
        return 1
    return 1 + min(fun2(m, i+1, j), fun2(m, i, j+1))


m = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(fun2(m, 0, 0))
2

# 3 no of ways to reach


def fun3(m, i, j):
    if i == len(m) - 1 and j == len(m[0]) - 1:
        return 1
    if i >= len(m) or j >= len(m[0]):
        return 0
    return fun3(m, i+1, j) + fun3(m, i, j+1)


m = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(fun3(m, 0, 0))

# 4 minimum steps with diagonal


def fun4(m, i, j):
    if i == len(m)-1 and j == len(m[0])-1:
        return 0
    if i >= len(m) or j >= len(m[0]):
        return float('inf')
    if i == j:
        return 1 + min(fun4(m, i+1, j+1), fun4(m, i+1, j), fun4(m, i, j+1))
    return 1 + min(fun4(m, i+1, j), fun4(m, i, j+1))


m = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(fun4(m, 0, 0))

# 5 with hudles


def fun5(m, i, j):
    if i == len(m)-1 and j == len(m[0])-1:
        return 0
    if i >= len(m) or j >= len(m[0]) or m[i][j] == -1:
        return float('inf')
    return 1 + min(fun5(m, i+1, j), fun5(m, i, j+1))


m = [[0, 1, 2],
     [3, 4, 5],
     [6, -1, 8]]

res = fun5(m, 0, 0)
if res == float('inf'):
    print("no path")
else:
    print(res)

# 6 with hudles and diagonal


def fun6(m, i, j):
    if i == len(m)-1 and j == len(m[0])-1:
        return 0
    if i >= len(m) or j >= len(m[0]) or m[i][j] == -1:
        return float('inf')
    if i == j:
        return 1 + min(fun6(m, i+1, j+1), fun6(m, i+1, j), fun6(m, i, j+1))
    return 1 + min(fun6(m, i+1, j), fun6(m, i, j+1))


m = [[0, 1, 2],
     [3, 4, 5],
     [6, -1, 8]]

res = fun6(m, 0, 0)
if res == float('inf'):
    print("no path")
else:
    print(res)

# minimum cost using recursions


def fun7(m, i, j):
    if i == len(m)-1 and j == len(m[0])-1:
        return m[i][j]
    if i >= len(m) or j >= len(m[0]):
        return float('inf')
    return m[i][j] + min(fun7(m, i+1, j), fun7(m, i, j+1))


m = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(fun7(m, 0, 0))
# 1-6 using memo and recursion


# 1
def fun(m, i, j, dp):
    if i == len(m) - 1 and j == len(m[0]) - 1:
        return 1
    if i >= len(m) or j >= len(m[0]):
        return float('inf')
    if dp[i][j] != float('inf'):
        return dp[i][j]
    dp[i][j] = 1+min(fun(m, i+1, j, dp), fun(m, i, j+1, dp))
    return dp[i][j]


m = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
dp = [[float('inf') for _ in range(len(m[0]))] for _ in range(len(m))]
print(fun(m, 0, 0, dp))

# 2


def fun2(m):
    r = len(m)
    c = len(m[0])
    dp = [[float('inf') for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[r-1][c-1]


m = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(fun2(m))

# 3


def fun3(m):
    r = len(m)
    c = len(m[0])
    dp = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[r-1][c-1]


m = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(fun3(m))


'''
#

'''
def is_palindrome(s):
    return s == s[::-1]


def min_cuts(s):
    if is_palindrome(s):
        return 0
    if len(s) == 1:
        return 0

    res = float('inf')
    for i in range(1, len(s)):
        if is_palindrome(s[:i]):
            res = min(res, 1 + min_cuts(s[i:]))
    return res


def min_cuts(s):
    n = len(s)
    dp = [[float('inf')] * n for _ in range(n)]

    def min_cuts_memo(s, i, dp):
        if i == n:
            return 0
        if dp[i] != float('inf'):
            return dp[i]
        if is_palindrome(s[:i+1]):
            dp[i] = 0
        else:
            dp[i] = float('inf')
            for j in range(i):
                if is_palindrome(s[j:i+1]):
                    dp[i] = min(dp[i], 1 + min_cuts_memo(s, j, dp))
        return dp[i]

    return min_cuts_memo(s, n - 1, dp)


s = input()
print(min_cuts(s))

s = input()
dp = [[-1]*len(s) for _ in range(len(s))]


def part(i, j):
    if i >= j or s[i:j+1] == s[i:j+1][::-1]:
        return 0
    ans = float('inf')
    for k in range(i, j):
        ans = min(ans, 1+part(i, k)+part(k+1, j))
    return ans


def part_dp(i, j):
    if i >= j or s[i:j+1] == s[i:j+1][::-1]:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = float('inf')
    for k in range(i, j):
        dp[i][j] = min(dp[i][j], 1+part_dp(i, k)+part_dp(k+1, j))
    return dp[i][j]


print(part(0, len(s)-1))
print(part_dp(0, len(s)-1), dp)
'''

# find the minim no of multiplications to multiply the matrices where the input is array of dimensions
'''
arr = list(map(int, input().split()))


def matrix_chain(arr, i, j):
    if i >= j:
        return 0
    ans = float('inf')
    for k in range(i, j):
        ans = min(ans, matrix_chain(arr, i, k) + matrix_chain(arr, k+1, j) + arr[i-1]*arr[k]*arr[j])
    return ans


print(matrix_chain(arr, 1, len(arr)-1))
'''

# find the max in a array like k is the max size of subarray and the max of subarray is replaced in the all elements of the subarray and then the sum of the array is returned in recursion


def max_sum(arr, k, i=0):
    if i >= len(arr):
        return 0
    max_in_subarray = max(arr[i:i+k])
    return max_in_subarray * k + max_sum(arr, k, i + k)


arr = list(map(int, input().split()))
k = int(input())
print(max_sum(arr, k))
