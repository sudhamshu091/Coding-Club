def maxProduct(arr):
    n = len(arr)
    max_end = 1
    min_end = 1
    MAX = 1
    flag = 0
    for i in range(0, n):
        if arr[i] > 0:
            max_end *= arr[i]
            min_end = min(min_end * arr[i], 1)
            flag = 1

        elif arr[i] == 0:
            max_end = 1
            min_end = 1
        else:
            temp = max_end
            max_end = max (min_end * arr[i], 1)
            min_end = temp * arr[i]
        if (MAX < max_end):
            MAX = max_end

    if flag == 0 and MAX == 1:
        return 0
    else:
        return MAX

print(maxProduct([-6,4,-5,8,-10,0,8]))
print(maxProduct([1,2,3,4,5,6,7,8,-9]))
