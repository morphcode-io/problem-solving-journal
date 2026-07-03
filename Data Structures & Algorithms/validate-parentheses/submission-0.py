class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }
        stack = []
        for c in s:
            if c not in mp:
                stack.append(c)
            else:
                if not stack or stack.pop() != mp[c]:
                    return False
        return len(stack) == 0
