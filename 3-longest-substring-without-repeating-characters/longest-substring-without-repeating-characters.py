class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        length=0
        ans=set()
        ans2=0
        for i in range(len(s)):
            while s[i] in ans:
                ans.remove(s[left])
                left+=1
            ans.add(s[i])
            ans2=max(ans2,i-left+1)
        return ans2
            


        