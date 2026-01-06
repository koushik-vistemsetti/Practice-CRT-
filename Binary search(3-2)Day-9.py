# time complexity: O(log n)
# space complexity: O(1) for iterative and O(log n) for recursive

def binary_search(n, key):
    l = 0
    h = len(n)-1
    while l <= h:
        mid = l+(h-l)//2
        if n[mid] == key:
            return mid
        elif n[mid] < key:
            l = mid+1
        else:
            h = mid-1
    return -1


def lower_bound(n, key, low, high):
    while low <= high:
        mid = low+(high-low)//2
        if n[mid] >= key:
            high = mid-1
        else:
            low = mid+1
    return n[low]


def upper_bound(n, key, low, high):
    while low <= high:
        mid = low+(high-low)//2
        if n[mid] > key:
            high = mid-1
        else:
            low = mid+1
    return n[low]


def binary_search_recusion(n, key, l, h):
    while l <= h:
        mid = l+(h-l)//2
        if n[mid] == key:
            return mid
        elif n[mid] < key:
            return binary_search(n, key, mid+1, h)
        else:
            return binary_search(n, key, l, mid-1)
    return -1


def square_root(x):
    l = 0
    h = x
    ans = -1
    while l <= h:
        mid = l+(h-l)//2
        if mid*mid == x:
            return mid
        elif mid*mid < x:
            ans = mid
            l = mid+1
        else:
            h = mid-1
    return ans


def koko_eating_bananas(piles, h):
    l = 1
    r = len(piles)-1
    ans = r
    while l <= r:
        mid = l+(r-l)//2
        total_hours = 0
        for pile in piles:
            total_hours += (pile + mid - 1) // mid
        if total_hours <= h:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans


def q1(piles, h):
    s = 0
    c = 0
    for i in range(0, len(piles)):
        s += piles[i]
        if s > h:
            c += 1
            s = piles[i]
        else:
            continue
    if s > 0:
        c += 1

    return c


def minimum_days_boques(l, m, k):
    if k*m > len(l):
        return -1
    l.sort()
    low = 1
    high = l[-1]
    while low <= high:
        mid = low+(high-low)//2
        c = 0
        days = 0
        for i in l:
            if i <= mid:
                c += 1
            else:
                days += c//k
                c = 0
        days += c//k
        if days >= m:
            high = mid-1
        else:
            low = mid+1
    return low


def first_last_occurrence(n, key):
    first = -1
    last = -1
    l = 0
    h = len(n)-1
    while l <= h:
        mid = l+(h-l)//2
        if n[mid] == key:
            first = mid
            h = mid-1
        elif n[mid] < key:
            l = mid+1
        else:
            h = mid-1
    l = 0
    h = len(n)-1
    while l <= h:
        mid = l+(h-l)//2
        if n[mid] == key:
            last = mid
            l = mid+1
        elif n[mid] < key:
            l = mid+1
        else:
            h = mid-1
    c = last-first+1
    return first, last, c


# def threshold(l,)

# n=[1,2,3,4,5,6,7,8]
# n = list(map(int, input('Enter the sorted elements: ').split()))
# key = int(input('Enter the element to be searched: '))
# key=5
# l = 0
# h = len(n)-1
# while l <= h:
#     mid = l+(h-l)//2
#     if n[mid] == key:
#         print(n[mid])
#     elif n[mid] < key:
#         l = mid+1
#     else:
#         h = mid-1
# print(-1)


# res = binary_search(n, key)
# # res1 = binary_search_recusion(n, key, 0, len(n)-1)
# if res != -1:
#     print(f'Element found at index {res}')
# else:

#     print('Element not found')
# print(first_last_occurrence(n, key))
# print(lower_bound(n, key, 0, len(n)-1))

# print(upper_bound(n, key, 0, len(n)-1)
#       if upper_bound(n, key, 0, len(n)-1) <= n[-1] else -1)
num = int(input('Enter a number to find square root: '))
print(square_root(num))
print(q1([3, 6, 7, 11], 8))
print(minimum_days_boques([1, 10, 3, 10, 2], 3, 3))
