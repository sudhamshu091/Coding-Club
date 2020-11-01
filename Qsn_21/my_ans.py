def rearrange(arr, n):
	for i in range(0, n):
		arr[i] += (arr[arr[i]] % n) * n
	for i in range(0, n):
		arr[i] = int(arr[i] / n)

arr = [1, 3, 4, 2, 0]
n = len(arr)
print("Input:",arr)
rearrange(arr, n)
print("Output:",arr)
