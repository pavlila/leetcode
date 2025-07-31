# set O(n)
class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()

        for i in nums:
            if i in visited:
                return True
            else:
                visited.add(i)
        return False
    
# length of set and list O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length_of_list = len(nums)
        length_of_set = len(set(nums))
        
        if length_of_list == length_of_set:
            return False
        return True