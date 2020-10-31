def repeatusingbin(A):
    xor = 0
    for i in A:
        xor ^= (1 << i)

    print("Odd elements: ")
    for i in A:
        if xor & (1 << i):
            print(i, end=' ')
            xor ^= (1 << i)

print(repeatusingbin([5,8,2,5,8,2,8,5,1,8,2]))
