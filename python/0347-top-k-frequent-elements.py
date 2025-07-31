# max heap O(n log n) <- heap build
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        heap = []
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res