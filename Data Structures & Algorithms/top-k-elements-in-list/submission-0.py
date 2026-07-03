class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter()
        for num in nums:
            count_nums[num] += 1

        heap = []
        for num, cnt in count_nums.items():
            heapq.heappush(heap, (-cnt, num))
        
        res = []
        print(heap)
        while len(res) < k:
            _, num = heapq.heappop(heap)
            res.append(num)
        return res
        