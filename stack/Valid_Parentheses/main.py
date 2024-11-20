class Solution:
    def isValid(self, s: str) -> bool:
        character = {
            '(' : ')', 
            '{' : '}',
            '[' : ']'
        }

        stack = []
        for c in s:
            if c in character:
                stack.append(c)
            else:
                if stack and character[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True

# Test
s = Solution()
print(s.isValid("()")) # Output: True
print(s.isValid("()[]{}")) # Output: True
print(s.isValid("(]")) # Output: False