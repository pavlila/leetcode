# hash map O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}

        for index, num in enumerate(numbers):
            if num in dict:
                return [dict[num] + 1, index + 1]
            dict[target - num] = index