def decode(str, K):
        size = 0
        for i in str:
            if i.isdigit():
                size *= int(i)    #i*i #2*2 = 4
            else:
                size += 1
        for i in reversed(str):
            K %= size
            if K == 0 and i.isalpha():
                return i
            if i.isdigit():
                size /= int(i)
            else:                 #hahahaha
                size -= 1         #12345678
print(decode('ha22',5))             #  ^
                                   #   |
#o/p:h                                       
