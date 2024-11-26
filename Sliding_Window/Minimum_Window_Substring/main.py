from typing import List
from collections import defaultdict

# sliding window
# time complexity : O(n)
# space complexity: O(m)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        countWindow = defaultdict(int)
        for c in t:
            countT[c] += 1

        l = 0
        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = float('infinity')

        for r in range(len(s)):
            countWindow[s[r]] += 1
            if s[r] in countT  and countWindow[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                countWindow[s[l]] -= 1
                if s[l] in countT and countWindow[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        if resLen == float('infinity'):
            return ""
        else:
            return s[l:r+1]
        


        
# test
s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
print(sol.minWindow(s, t)) # Expect "BANC"