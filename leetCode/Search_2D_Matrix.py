
class Solution(object):

    def matrix_mapping(self, index, n, matrix):
        row_num = index//n
        colum_num = index % n
        return matrix[row_num][colum_num]

    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        low = 0
        high = m*n - 1
        while low <= high:
            mid = (low+high) // 2
            guess = self.matrix_mapping(mid, n, matrix)
            if(guess == target):
                return True
            if(guess > target):
                high = mid-1
            else:
                low = mid+1
        return False


s = Solution()
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 7))
