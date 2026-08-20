class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums=0
        n=len(nums)
        for i in range(k):
            sums+=nums[i]
        avg=sums/k
        max_count=avg
        for i in range(1,n-k+1):
            sums=sums-nums[i-1]+nums[i+k-1]
            avg=sums/k
            max_count=max(avg,max_count)
        return max_count
           

       
            