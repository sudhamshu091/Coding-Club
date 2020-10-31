list = [1,2,3,4,5,6,7,8,12,34,46,3646,2535]
list1 =[0]
x,y=0,1
while y < max(list):
    x,y = y,x+y
    list1.append(y)
c = [value for value in list1 if value in list]
print(c)
print(len(c))
