class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            lplusr = numbers[l] +  numbers[r]
            if lplusr == target:
                return [l + 1, r + 1]
            elif lplusr < target:
                l = l + 1
            else:
                r = r - 1


        return [] 