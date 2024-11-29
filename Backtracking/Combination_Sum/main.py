from typing import List

# Backtracking(Optimal)
# time complexity: O(n * (target/m))
# space complexity: O(target/m)
# m is the min value in nums
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, total, ans):
            if total == target:
                # 如果沒有使用copy()，res的答案會根據ans的改變一起改變
                res.append(ans.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                ans.append(nums[j])
                dfs(j, total + nums[j], ans)
                ans.pop()

        dfs(0, 0, [])
        return res
                
            
# test
nums = [2,3,6,7]
target = 7
sol = Solution()
print(sol.combinationSum(nums, target)) # expect [[2,2,3],[7]]