class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
                
        return count

# Test
s = "abc"
sol = Solution()
print(sol.countSubstrings(s)) # 3
s = "aaa"
print(sol.countSubstrings(s)) # 6
s = "aba"
print(sol.countSubstrings(s)) # 4
s = "abba"
print(sol.countSubstrings(s)) # 6
s = "abccba"
print(sol.countSubstrings(s)) # 9
