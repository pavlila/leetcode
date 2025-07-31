# O(log n)
class Solution:
    def reverse(self, x: int) -> int:
        ax = abs(x)
        sax = str(ax)
        rsax = sax[::-1]

        while rsax[0] == 0:
            rsax = rsax[1:]

        ret = int(rsax)
        if x < 0:
            ret *= -1
            
        if ret < -2**31 or ret > 2**31 -1:
            return 0
        return ret