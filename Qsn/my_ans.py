def findpairkdiff(a, diff):
    a.sort()
    i = j = 0
    length = len(a)
    while i < length and j < length:
        while i < length - 1 and a[i] == a[i + 1]:
            i = i + 1
        while j < length - 1 and a[j] == a[j + 1]:
            j = j + 1
        if a[j] - a[i] > diff:
            i = i + 1
        elif a[j] - a[i] < diff:
            j = j + 1
        else:
            print((a[j], a[i]))
            i = i + 1
            j = j + 1
findpairkdiff([1, 5, 2, 2, 2, 5, 5, 4], 3)
