class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        total=0
        ans=float("inf")

        for i in range(len(nums)):
            total+=nums[i]
            while total>=target:
                ans=min(ans,i-left+1)
                total-=nums[left]
                left+=1
        return ans if ans!=float("inf") else 0

        