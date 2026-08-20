class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.check(s, left + 1, right) or self.check(s, left, right - 1)

            left += 1
            right -= 1

        return True

    def check(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
            


        