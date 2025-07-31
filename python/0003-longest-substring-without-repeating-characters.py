# set O(n^2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for i, val in enumerate(s):
            visited = set()
            visited.add(val)

            for j in range(i + 1, len(s)):
                if s[j] in visited:
                    if len(visited) > longest:
                        longest = len(visited)
                    break
                visited.add(s[j])

            if len(visited) > longest:
                longest = len(visited)
        
        return longest