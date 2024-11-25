from typing import List
from collections import defaultdict

# Hash Set
# time complexity: O(n)
# space complexity: O(n)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if nums is None or len(nums)==0:
#             return 0
#         num_set = set(nums)
#         max_seq_len = 0

#         for num in num_set:
#             if (num-1) not in num_set:
#                 seq_len = 1
#                 while (num+seq_len) in num_set:
#                     seq_len += 1
#                 max_seq_len = max(max_seq_len, seq_len)
#         return max_seq_len


# Hash Map
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num-1] + mp[num+1] + 1
                mp[num - mp[num-1]] = mp[num] 
                mp[num + mp[num+1]] = mp[num]
                res = max(res, mp[num])

        return res  

# Test
nums = [100, 4, 200, 1, 3, 2]
sol = Solution()
print(sol.longestConsecutive(nums)) # Expect 4           