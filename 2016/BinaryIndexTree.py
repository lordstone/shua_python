class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.n = len(matrix)
        if self.n == 0:
            return  # error
        self.m = len(matrix[0])
        self.BIT = []
        self.matrix = matrix
        for i in range(self.n):
            tmp = [0] * self.m
            self.BIT.append(tmp)
            for j in range(self.m):
                self.updatex(i, j, matrix[i][j])

    def updatex(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        idx = col + 1
        while idx <= self.m:
            self.BIT[row][idx - 1] += val
            idx += (idx & - idx)


    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        idx = col + 1
        while idx <= self.m:
            self.BIT[row][idx - 1] += diff
            idx += (idx & - idx)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in range(row1, row2 + 1):
            tmp = self.getSum(i, col2 + 1)  # input idx
            if col1 != 0:
                tmp -= self.getSum(i, col1)  # col1 - 1 + 1
            res += tmp
        return res

    def getSum(self, row, idx):
        res = 0
        while idx != 0:
            res += self.BIT[row][idx - 1]
            idx -= idx & (- idx)
        return res


# Your NumMatrix object will be instantiated and called as such:

# matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
# matrix = [[2, 4], [-3, 5]]
matrix = [[0, -5, 9, 1, -8, 5, 8, 1, 1, 5]]
numMatrix = NumMatrix(matrix)
print(numMatrix.sumRegion(0,5,0,9))
# numMatrix.update(1,1,2)
# print(numMatrix.sumRegion(0,0,1,1))
