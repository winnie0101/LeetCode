from collections import defaultdict
from typing import List

# Sorting
# time complexity: O(nlogn)
# space complexity: O(n)
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = defaultdict(int)
#         for n in nums:
#             count[n] += 1

#         # count = dict(sorted(count.items(), key=lambda i:i[1], reverse=True))

#         # res = []
#         # for i, key in enumerate(count):
#         #     if i < k:
#         #         res.append(key)

#         arr = []
#         for key, cnt in count.items():
#             arr.append([cnt, key])
#         arr.sort()

#         res = []
#         for i in range(k):
#             res.append(arr.pop()[1])
#         return res


# Heap
# time complexity: O(nlogk)
# space complexity: O(n + k)
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = defaultdict(int)
#         for n in nums:
#             count[n] += 1

#         heap = []
#         for key, cnt in count.items():
#             heapq.heappush(heap, (cnt, key))
#             if len(heap) > k:
#                 heapq.heappop(heap)

#         res = []
#         for i in range(k):
#             res.append(heapq.heappop(heap)[1])
#         return res


# Bucket Sort
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        freq = [[] for i in range(len(nums) + 1)]
        for key, cnt in count.items():
            freq[cnt].append(key)

        res = []
        for i in range (len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

# Test
nums = [1,1,1,2,2,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k)) # Expect [1,2]