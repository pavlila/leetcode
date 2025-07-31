# hash map O(m + n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        for i in s:
            if i in map1:
                map1[i] += 1
            else:
                map1[i] = 1

        map2 = {}
        for i in t:
            if i in map2:
                map2[i] += 1
            else:
                map2[i] = 1

        if map1 == map2:
            return True
        return False 