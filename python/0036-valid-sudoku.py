# set indexing O(1) <- always 9x9
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        nines = [set() for _ in range(9)]

        for i, row in enumerate(board):
            seen = set()
            
            for index, val in enumerate(row):
                if val != '.':
                    block_index = (i // 3) * 3 + (index // 3)

                    if val in nines[block_index]:
                        return False
                    else:
                        nines[block_index].add(val)

                    if val in cols[index]:
                        return False
                    else:
                        cols[index].add(val)

                    if val in seen:
                        return False
                    else:
                        seen.add(val)

        return True