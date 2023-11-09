class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        for i in range(1, rowIndex + 1):
            previous_row = triangle[-1]
            triangle.append([1] + [previous_row[i2 - 1] + previous_row[i2] for i2 in range(1, i)] + [1])
        return triangle[rowIndex]