"""
A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in
non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If
such an index does not exist, return -1.

You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

- BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
- BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the
matrix is rows x cols.

Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that
attempt to circumvent the judge will result in disqualification.

For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary
matrix directly.

Example:
Input: mat = [[0,0],[1,1]]
Output: 0
Note: Visualize to understand.

Tag: fb R43/50, 1428/2927, R1801/2936

Note: Not testable in local since there is external API call
"""

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


def leftmost_column_with_one(binary_matrix: 'BinaryMatrix') -> int:
    def bs(row):
        beg = 0
        end = cols-1

        while beg <= end:
            mid = (beg+end)//2
            if binaryMatrix.get(row, mid) == 1:
                end = mid-1
            else:
                beg = mid+1
        return beg

        ans = float('inf')
        rows, cols = binaryMatrix.dimensions()
        for row in range(rows):
            ans = min(ans, bs(row))
        if ans == cols:
            return -1
        return ans


"""
Complexity
if N is the number of rows and M is the number of columns
Time complexity ~ O(N*log(M))
Space complexity ~ O(1)
"""