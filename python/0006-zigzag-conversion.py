# matrix O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[0 for i in range(len(s))] for i in range(numRows)]

        col = 0
        row = 0
        first = True

        for char in s:
            matrix[row][col] = char

            if numRows == 1:
                return s
            
            if col % (numRows - 1) == 0 and row < numRows - 1:
                if first:
                    row = 0
                    first = False
                row += 1
            elif col % (numRows - 1) == 0:
                col += 1
                row = numRows - 2
                first = True
            else:
                col += 1
                row -= 1

        res = ""
        for row in matrix:
            for i in row:
                if i != 0:
                    res += i

        return res