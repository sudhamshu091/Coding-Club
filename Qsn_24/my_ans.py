class Permutation:
    def isidealpermutation(self, A: List[int]) -> bool:
        left = A[0]
        for k in range(2, len(A)):
            if left > A[i]:
                return False
            else:
                left = max(left, A[k - 1])
        return true
