from collections import defaultdict
from typing import List

# two pointer
# time complexity: O(n^2)
# space complexity: O(1) or O(n)
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         print(nums)
#         res = set()

#         for i in range(len(nums)):
#             l, r = i+1, len(nums)-1
#             total = 0
#             while l < r:
#                 total = nums[l] + nums[r] + nums[i]
#                 if total == 0:
#                     res.add(tuple([nums[l], nums[i], nums[r]]))
#                     l += 1
#                 elif total < 0:
#                     l += 1
#                 else:
#                     r -= 1

#         return [list(r) for r in res]
            

# hash map
# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:   
        nums.sort()
        count = defaultdict(int)  
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1
                if j-1 > i and nums[j] == nums[j-1]:
                    continue
                
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i+1, len(nums)):
                count[nums[j]] += 1

        return res
        

# Test
nums = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(nums)) # Expect [[-1,-1,2],[-1,0,1]]

nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
sol = Solution()
print(sol.threeSum(nums)) 
# Expect [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]