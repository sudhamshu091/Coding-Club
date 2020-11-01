def maxSum(a, i, n, last_val = float("-inf")):
    if i == n:
        return 0
    excl = maxSum(a, i + 1, n, last_val)
    incl = 0
    if last_val + 1 != i:
        incl = maxSum(a, i + 1, n, i) + a[i]
    return max(incl, excl)
print(maxSum([1, 2, 9, 4, 5, 0, 4, 11, 6], 0, len([1, 2, 9, 4, 5, 0, 4, 11, 6])))
