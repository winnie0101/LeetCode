from typing import List


# two pointer
# time complexity: O(n)
# space complexity: O(1)
# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         if len(heights) == 0:
#             return 0
#         max_width = len(heights)-1
#         max_area = 0
#         for width in range(max_width, 0, -1):
#             left = 0
#             right = left + width
#             while right < len(heights):
#                 area = width * min(heights[left], heights[right])
#                 max_area = max(max_area, area)
#                 left += 1
#                 right += 1

#         return max_area


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_area = 0

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Test
heights = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(heights)) # Expect 49


        