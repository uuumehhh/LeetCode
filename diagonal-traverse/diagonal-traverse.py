class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 0:
            return []

        N, M = len(matrix), len(matrix[0])
        result, inter = [], []
        
        for d in range(N + M - 1):
            inter.clear()
            if d < M:
                r, c = 0, d
            else:
                r, c = d - M + 1, M - 1
            while r < N and c > -1:
                inter.append(matrix[r][c])
                r += 1
                c -= 1
            if d % 2 == 0:
                result.extend(inter[::-1])
            else:
                result.extend(inter)
        return result
