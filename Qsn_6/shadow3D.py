def shadow3D(x):
    N = len(x)
    ans = 0

    for i in range(N):
        row = 0
        col = 0
        for j in range(N):
            if x[i][j]: ans += 1  # top shadow
            row = max(row, x[i][j])
            col = max(col, x[j][i])

        ans += row + col

    return ans
print(shadow3D([[1,2],[3,4]]))
