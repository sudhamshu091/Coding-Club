x = [[1,2],[3,7],[1,1]]
print(x)
a =0
list = []
for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] not in list:
                list.append(x[i][j])
                a = a + x[i][j]+1
print(a+3)
