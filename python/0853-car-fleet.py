# O(n log n) <- sorting
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        res = 0
        val = 0

        for p, s in pair:
            curr = (target - p) / float(s)
            
            if curr > val:
                res += 1
                val = curr

        return res