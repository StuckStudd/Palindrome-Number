class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x = 121
        s = str(x)
        for i in range(len(s)):
            print(s[i])
            print(s [ -i - 1])
            print()
            if s[i] !=  s [ -i - 1]:
                return False
        return True
 
q1 = Solution()
print(q1.isPalindrome(121))
# s = "abc"
# print(s[-1])