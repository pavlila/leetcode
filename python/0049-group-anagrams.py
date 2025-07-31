class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        options = []

        for word in strs:
            key = sorted(word)
            
            if key in options:
                index = options.index(key)
                res[index].append(word)
            else:
                options.append(key)
                res.append([word])

        return res