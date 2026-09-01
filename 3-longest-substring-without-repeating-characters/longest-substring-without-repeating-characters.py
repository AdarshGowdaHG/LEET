class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        ans=set()
        len2=0
        for i in range(len(s)):
            while s[i] in ans:
                ans.remove(s[left])
                left+=1
            ans.add(s[i])
            len2=max(len2,i-left+1)
        return len2
       