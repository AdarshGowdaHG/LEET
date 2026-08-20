class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        suma=0
        n=len(nums)
        for i in range(k):
            suma+=nums[i]
        avd=suma
        for i in range(1,n-k+1):
            suma=suma-nums[i-1]+nums[i+k-1]
            avd=max(avd,suma)
        return avd/k

           

       
            