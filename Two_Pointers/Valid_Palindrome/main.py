# two pointer
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s)-1
        if l == r:
            return True

        while l < r:
        
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
                
            while l < r and not self.isAlphaNum(s[r]):
                r -= 1
               
            char_l = s[l].lower()
            char_r = s[r].lower()
            if char_l == char_r:
                l += 1
                r -= 1
            else:
                return False

        return True

    def isAlphaNum(self, c):
        c = c.lower()
        return (ord(c) in range(ord('a'), ord('z')+1) or ord(c) in range(ord('0'), ord('9')+1))

    
# Test
s = "Was it a car or a cat I saw?"
sol = Solution()
print(sol.isPalindrome(s)) # True

s = " "
print(sol.isPalindrome(s)) # True

s = ".,"
print(sol.isPalindrome(s)) # True
         