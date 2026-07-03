class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        area = 0
        maxLeft = 0
        maxRight = height[-1]
        l, r = 0, len(height) - 1
        
        while l < r:
            if height[l] < height[r]:
               maxLeft = max(maxLeft, height[l])
               area += maxLeft - height[l]
               l += 1
            else:
               maxRight = max(maxRight, height[r])
               area += maxRight - height[r]
               r -= 1
            
            if res < area:
                res = area 

        return res