class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans=0
        nsl=[]
        nsr=[-1]*(len(arr))
        stack=[]
        stack1=[]
        for i in range(len(arr)):
            if len(stack)==0:
                nsl.append(-1)
            elif arr[stack[-1]]<arr[i]:
                nsl.append(stack[-1])
            else:
                while len(stack)!=0 and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                if len(stack)==0:
                    nsl.append(-1)
                else:
                    nsl.append(stack[-1])
            stack.append(i)
            
        # stack=[]
        for i in range(len(arr)-1,-1,-1):
            if len(stack1)==0:
                nsr[i]=len(arr)
            elif arr[stack1[-1]]<=arr[i]:
                nsr[i]=stack1[-1]
            else:
                while len(stack1)!=0 and arr[stack1[-1]]>arr[i]:
                    stack1.pop()
                if len(stack1)==0:
                    nsr[i]=len(arr)
                else:
                    nsr[i]=stack1[-1]
            stack1.append(i)
        ans=0
        net=0
        mod=1000000007
        for i in range(len(arr)):
            n=nsr[i]-nsl[i]-1
            m=((n)*(n+1))//2
            x=i-nsl[i]-1
            y=nsr[i]-i-1
            a=((x)*(x+1))//2
            b=((y)*(y+1))//2
            net=m-a-b
            ans+=((net%mod)*(arr[i]%mod))%mod
            ans=ans
        return ans%mod
