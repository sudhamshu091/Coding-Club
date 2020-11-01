from math import sqrt
def decode(a):
    n = int((sqrt(8 * len(a) + 1) + 1) / 2)
    A = [0] * n
    if n == 1:
        A[0] = a[0]
    elif n == 2:
        A[0] = a[0] - a[1]
    else:
        A[0] = (a[0] + a[1] - a[n - 1]) // 2
    for i in range(1, n):
        A[i] = a[i - 1] - A[0]
    print(A)
decode([3, 4, 5, 5, 6, 7])
