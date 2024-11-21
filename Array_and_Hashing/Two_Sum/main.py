from typing import List

# Hash Map(two pass)
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            dict[n] = i

        for i, n in enumerate(nums):
            diff = target-n
            if diff in dict and dict[diff] != i:
                return [i, dict[diff]]


# test
nums = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target)) # Expect [0, 1]