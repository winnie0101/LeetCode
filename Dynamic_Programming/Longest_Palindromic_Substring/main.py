
# brute force
# time complexity : O(n^3)
# space complexity: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        res = ""

        for l in range(len(s)):
            for r in range(len(s)-1, l-1, -1):
                i, j = l, r
                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1

                if i >= j and (r-l+1) > max_len:
                    max_len = r-l+1
                    res = s[l:r+1]

        return res

# two pointers
# time complexity: O(n^2)
# space complexity: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        resIdx = 0
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1

            # even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1

        return s[resIdx : resIdx + maxLen]

# test
s = "babad"
sol = Solution()
print(sol.longestPalindrome(s)) # expect "bab" or "aba"
s = "cbbd"
print(sol.longestPalindrome(s)) # expect "bb"
s = "a"
print(sol.longestPalindrome(s)) # expect "a"
