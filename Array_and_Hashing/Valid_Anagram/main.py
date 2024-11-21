

# Hash Table
# time complexity: O(n+m)
# space complexity: O(1) since we have at most 26 different characters.
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         character_dict = {}
#         for i in range(len(s)):
#             if s[i] in character_dict:
#                 character_dict[s[i]] += 1
#             else:
#                 character_dict[s[i]] = 1
#             if t[i] in character_dict:
#                 character_dict[t[i]] -= 1
#             else:
#                 character_dict[t[i]] = -1

#         for key in character_dict:
#             if character_dict[key] != 0:
#                 return False
#         return True

# Sorting
# time complexity: O(nlogn + mlogm)
# space complexity: O(1) or O(n+m)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
            

# Test
s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t)) # Expect True