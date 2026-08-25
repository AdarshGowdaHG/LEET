class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        list=[]
        sum=0
        n=len(nums)
        i=0
        if 2*k+1>n:
            return [-1]*n
        while(i<k):
            list.append(-1)
            i+=1
        i=0
        while(i<2*k+1):
            sum+=nums[i]
            i+=1
        avg=sum//(2*k+1)
        list.append(avg)

        for i in range(k+1,n-k):
            sum=sum-nums[i-k-1]+nums[i+k]
            avg=sum//(2*k+1)
            list.append(avg)
        while len(list)<n:
            list.append(-1)
        return list


        