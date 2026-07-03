class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        acc = 0
        maxLeft = 0
        maxRight = height[-1]
        l, r = 0, len(height) - 1
        
        while l < r:
            if height[l] < height[r]:
               maxLeft = max(maxLeft, height[l])
               acc += maxLeft - height[l]
               l += 1
            else:
               maxRight = max(maxRight, height[r])
               acc += maxRight - height[r]
               r -= 1
            res = max(res, acc)

        return res