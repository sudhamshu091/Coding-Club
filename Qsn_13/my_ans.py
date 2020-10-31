from collections import deque
def Q(n):
    q = deque()
    q.append('1')

    for i in range(n):
        first = str(q.popleft())
        q.append(first + '0')
        q.append(first + '1')
        print(first)
print(Q(5))
