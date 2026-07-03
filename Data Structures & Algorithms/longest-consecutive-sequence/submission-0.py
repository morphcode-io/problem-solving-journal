class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                i = 1
                while num + i in nums:
                    i += 1
                res = max(res, i)

        return res