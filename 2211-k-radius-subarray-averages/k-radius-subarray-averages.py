class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        curr_sum=0
        i=0
        n=len(nums)
        if 2*k+1>n:
            return [-1]*n
        while i<k:
            ans.append(-1)
            i+=1
        i=0
        while(i<2*k+1):
            curr_sum+=nums[i]
            i+=1
        avg=curr_sum//(2*k+1)
        ans.append(avg)

        for i in range(k+1,n-k):
            curr_sum=curr_sum-nums[i-k-1]+nums[i+k]
            avg=curr_sum//(2*k+1)
            ans.append(avg)
        while len(ans)<n:
            ans.append(-1)
        return ans
        
