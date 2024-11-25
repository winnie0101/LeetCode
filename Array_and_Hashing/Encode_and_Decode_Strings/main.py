from typing import List

# time complexity: O(m) m is the sum of lengths of all the strings
# space complexity: O(1)
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
            
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            strLen = int(s[i:j])
            i = j+1
            j = i+strLen
            res.append(s[i:j])
            i = j

        return res
                    
                  

# Test
strs = ["hello", "world"]
sol = Solution()
encoded = sol.encode(strs)
print(encoded) # Expect "5#hello5#world"
print(sol.decode("5#hello5#world")) # Expect ["hello", "world"]

strs = ["we","say",":","yes","!@#$%^&*()"]
sol = Solution()
encoded = sol.encode(strs)
print(encoded) # Expect "2#we3#say1#:3#yes10#!@#$%^&*()"
print(sol.decode("2#we3#say1#:3#yes10#!@#$%^&*()")) # Expect ["we","say",":","yes","!@#$%^&*()"]