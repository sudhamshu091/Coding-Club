n = int(input("Enter a number:"))
binary = bin(n)
string = str(binary)
if '11' in string:
    print(1)
else:
    print(0)
