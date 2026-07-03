class Solution:
    def isAlph(self, c: str) -> bool:
        return ord(c) <= ord("z") and ord(c) >= ord("a") or ord(c) <= ord("Z") and ord(c) >= ord("A") or ord(c) >= ord("0") and ord(c) <= ord("9")

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlph(s[l]):
                l += 1
            while l < r and not self.isAlph(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
    
        return True