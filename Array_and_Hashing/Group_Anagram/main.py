from typing import List
from collections import defaultdict

# Sorting
# time complexity: O(m * nlogn)
# space complexity: O(m * n)
# m is the number of strings
# n is the lenght of longest string
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             sortedS = ''.join(sorted(s))
#             res[sortedS].append(s)
#         return list(res.values())

# Hash table
# time complexity: O(m * n)
# space complexity: O(m)
# m is the number of strings
# n is the lenght of longest string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            # 用字串中每個字母的數量來作為key
            for c in s:
                count[ord(c)-ord("a")] += 1

            res[tuple(count)].append(s)
        return list(res.values())


# Test
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(strs)) # Expect [["eat","tea","ate"],["tan","nat"],["bat"]]     