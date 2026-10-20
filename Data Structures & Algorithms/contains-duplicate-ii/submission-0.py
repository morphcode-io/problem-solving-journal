class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = defaultdict(set)

        for i, num in enumerate(nums):
            if num in mp and len(mp[num]) >= 1:
                for j in mp[num]:
                    if abs(i - j) <= k:
                        return True

            mp[num].add(i)
        return False