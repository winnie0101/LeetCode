from typing import List

# Division
# time complexity: O(n)
# space complexity: O(n)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         zero_cnt = 0
#         all_product = 1
#         for num in nums:
#             if num == 0:
#                 zero_cnt += 1
#                 continue
#             all_product *= num

#         res = [0] * len(nums)
#         if zero_cnt >= 2:
#             return res
#         for i in range(len(nums)):
#             if zero_cnt==1 and nums[i] == 0:
#                 res[i] = all_product
#             elif zero_cnt==1 and nums[i] != 0:
#                 continue
#             else:
#                 res[i] = int(all_product/nums[i])
#         return res


# Prefix & Suffix
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n

        pref[0] = 1
        suff[n-1] = 1
        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(n-1, 0, -1):
            suff[i-1] = nums[i] * suff[i]

        for i in range(n):
            res[i] = pref[i] * suff[i]

        return res

# Test
nums = [1,2,3,4]
sol = Solution()
print(sol.productExceptSelf(nums)) # Expect [24,12,8,6]