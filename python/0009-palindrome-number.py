# reverse string O(log n)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        string = str(x)
        rstring = string[::-1]

        if string == rstring:
            return True
        return False