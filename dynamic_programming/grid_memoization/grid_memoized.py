def grid_traveler(m,n,memo = {}):
    if (m,n) in memo:
        return memo[(m,n)]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[(m,n)] = grid_traveler(m-1, n, memo) + grid_traveler(m, n - 1, memo)

    return memo[(m,n)]


m,n = 2,3

print(grid_traveler(2,3))
print(grid_traveler(18,18))