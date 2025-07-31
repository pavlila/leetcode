# O(n log n) <- sorting
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        longest = 0
        curr = 1

        for index, num in enumerate(nums):
            if index == len(nums) - 1:
                if curr > longest:
                    longest = curr

                break

            if nums[index + 1] == nums[index] + 1:
                curr += 1

                if curr > longest:
                    longest = curr
                    
            elif nums[index + 1] == nums[index]:
                continue
            else:
                curr = 1

        return longest