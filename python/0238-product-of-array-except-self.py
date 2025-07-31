# prefix and sufix array O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        sufixes = []

        num = 1
        for val in nums:
            num = val * num
            prefixes.append(num)

        num = 1
        for val in reversed(nums):
            num = val * num
            sufixes.append(num)
            
        sufixes = list(reversed(sufixes))

        res = []
        for i in range(len(nums)):
            if i == len(nums) - 1:
                res.append(prefixes[i - 1])
            elif i == 0:
                res.append(sufixes[i + 1])
            else:
                res.append(prefixes[i - 1] * sufixes[i + 1])

        return res