from typing import List

# sliding window
# time complexity : O(n)
# space complexity : O(m)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         seq = set()
#         l = 0
#         max_len = 0

#         for r in range(len(s)):
#             while s[r] in seq:
#                 seq.remove(s[l])
#                 l += 1

#             seq.add(s[r])
#             max_len = max(max_len, r - l +1)
#         return max_len


# sliding window
# time complexity : O(n)
# space complexity : O(m)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)
            mp[s[r]] = r
            res = max(res, r-l+1)
        return res


# Test
s = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s)) # Expect 3