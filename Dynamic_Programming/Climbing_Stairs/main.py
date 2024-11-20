# Recursive
# time complexity: O(2^n)
# space complexity: O(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2 :
#             return n

#         return self.climbStairs(n-1) + self.climbStairs(n-2)

# Dynamic(bottom-up)
# time complexity: O(n)
# space complexity: O(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         step = [-1] * (n+1)
#         if n <= 2:
#             return n
#         step[1], step[2] = 1, 2
#         for i in range(3, n+1):
#             step[i] = step[i-1] + step[i-2]

#         return step[n]

# Dynamic(top-down)
# time complexity: O(n)
# space complexity: O(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         step = [-1] * n
#         def dfs(i):
#             if i >= n:
#                 return i == n
#             if step[i] != -1:
#                 return step[i]
#             step[i] = dfs(i+1) + dfs(i+2)
#             return step[i]

#         return dfs(0)

# Dynamic(space optimized)
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(1, n):
            temp = one
            one = one + two
            two = temp

        return one


# Test
n = 5
sol = Solution()
print(sol.climbStairs(n)) # Expect 8
