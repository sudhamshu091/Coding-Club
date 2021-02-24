class Solution(object):
    def smallestdiff(self, A, K):
        return max(0, max(A) - min(A) - 2*K)

  
#s = Solution()
#print(s.smallestdiff([0,10],2))
#6
