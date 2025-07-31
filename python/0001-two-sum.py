# brute-force O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
# hash map O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for indx, val in enumerate(nums):
            res = target - val
            if res in dict:
                return dict[res], indx 
            dict[val] = indx