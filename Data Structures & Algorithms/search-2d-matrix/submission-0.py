class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #row = index // number_of_columns
        #col = index % number_of_columns
        rows=len(matrix)
        cols=len(matrix[0])

        left=0
        right=(rows*cols)-1

        while left <= right:

            mid = (left + right) // 2

            # Convert 1D index -> 2D position
            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False

        