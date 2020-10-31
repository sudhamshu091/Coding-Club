INT_BITS = 32
def leftRotate(N, K):
    return (N << K)|(N >> (INT_BITS - K))

def rightRotate(N, K):
	return (N >> K)|(N << (INT_BITS - K)) & 0xFFFFFFFF

N = 127
K = 3

print("Left Shift of",N,"by",K,"is",end=" ")
print(bin(leftRotate(N, K)))

print("Right Shift of",N,"by",K,"is",end=" ")
print(bin(rightRotate(N, K)))
