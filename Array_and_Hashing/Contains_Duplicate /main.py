from typing import List

# Hash set
# time complexity: O(n)
# space complexity: O(n)
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for i in range(len(nums)):
#             if nums[i] in seen:
#                 return True
#             else:
#                 seen.add(nums[i])

#         return False

# Hash set Length
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


# Sorting
# time complexity: O(nlogn)
# space complexity: O(1) or O(n)
# 如果sort用原地排序in-place 就是O(1) 例如Bubble Sort, Quick Sort
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()

#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:
#                 return True
#         return False


# Test
nums = [1,2,3,1]
sol = Solution()
print(sol.hasDuplicate(nums)) # Expect True