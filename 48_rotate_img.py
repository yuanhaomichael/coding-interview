class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:]

        # IDEA: reverse the whole matrix diagonally from upper left to lower right (transpose), then reverse each row
        # TIME: O(n^2) total number of cells is n^2
        # SPACE: O(1) b/c in place
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # trasponse
        for i in range(n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j] [i] = temp
        
        for row in matrix:
            self.reverse(row)
        
    
    def reverse(self, arr):
        i = 0
        j = len(arr) - 1
        while j > i:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1