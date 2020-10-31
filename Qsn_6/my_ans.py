x = [[1,2],[3,4]]
print(x)
a =0
for i in range(len(x)):
        for j in range(len(x[0])):
            a = a + x[i][j] + 1
print(a+3)
