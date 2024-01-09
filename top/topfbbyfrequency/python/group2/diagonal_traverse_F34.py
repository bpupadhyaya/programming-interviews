"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Note: Visualize to understand, diagonals traversal without lifting a pen

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
-10^5 <= mat[i][j] <= 10^5

Tag: F34/50
"""


def find_diagonal_order(matrix: list[list[int]]) -> list[int]:
    d = {}
    # loop through matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # if no entry in dictionary for sum of indices aka the diagonal, create one
            if i + j not in d:
                d[i+j] = [matrix[i][j]]
            else:
                # If already passed over this diagonal, keep adding elements to it.
                d[i+j].append(matrix[i][j])
        # Done with the pass, now build our answer array
    ans = []
    # look at the diagonal and each diagonal's elements
    for entry in d.items():
        # each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
        # snake time, look at the diagonal level
        if entry[0] % 2 == 0:
            # Here we append in reverse order because it's an even numbered level/diagonal.
            [ans.append(x) for x in entry[1][::-1]]
        else:
            [ans.append(x) for x in entry[1]]
    return ans


def main():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(find_diagonal_order(mat))


if __name__ == "__main__":
    main()
