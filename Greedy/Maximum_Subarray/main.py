from typing import List

# kadane's algo
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curSum = nums[0]

        for n in nums[1:]:
            curSum = max(curSum + n, n)
            maxSum = max(maxSum, curSum)

        return maxSum
        
# dynamic
# time complexity: O(n)
# space complexity:O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])

        return max(dp)

# Test
nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
print(sol.maxSubArray(nums)) # 6
