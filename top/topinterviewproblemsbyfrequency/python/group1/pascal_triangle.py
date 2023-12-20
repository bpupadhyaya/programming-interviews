"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
1
1 1
1 2 1
1 3 3 1

Example:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Tag: Tag: R27/145
"""


def generate_pascal_triangle_using_recursion(num_rows: int) -> list[list[int]]:
    if num_rows == 0:
        return []
    if num_rows == 1:
        return [[1]]

    prev_rows = generate_pascal_triangle_using_recursion(num_rows - 1)
    new_row = [1] * num_rows

    for i in range(1, num_rows - 1):
        new_row[i] = prev_rows[-1][i-1] + prev_rows[-1][i]
    prev_rows.append(new_row)
    return prev_rows


def generate_pascal_triangle_using_combinatorial_formula(num_rows: int) -> list[list[int]]:
    result = []
    if num_rows == 0:
        return result
    first_row = [1]
    result.append(first_row)
    for i in range(1, num_rows):
        prev_row = result[i-1]
        current_row = [1]
        for j in range(1, i):
            current_row.append(prev_row[j-1] + prev_row[j])
        current_row.append(1)
        result.append(current_row)
    return result


def generate_pascal_triangle_using_dynamic_programming_1d(num_rows: int) -> list[list[int]]:
    if num_rows == 0:
        return []
    if num_rows == 1:
        return [[1]]
    prev_rows = generate_pascal_triangle_using_dynamic_programming_1d(num_rows - 1)
    prev_row = prev_rows[-1]
    current_row = [1]
    for i in range(1, num_rows - 1):
        current_row.append(prev_row[i-1] + prev_row[i])
    current_row.append(1)
    prev_rows.append(current_row)
    return prev_rows


def main():
    num_rows = 5
    print(generate_pascal_triangle_using_dynamic_programming_1d(num_rows))


if __name__ == "__main__":
    main()


"""
Intuition
The problem of generating Pascal's triangle can be approached in various ways.
Here are some approaches and their intuition to solve the problem:

Approach 1: Using Recursion
Intuition: In Pascal's triangle, each element is the sum of the two elements directly above it. We can 
use a recursive approach to generate the triangle. The base case is when numRows is 1, in which case we 
return [[1]]. Otherwise, we recursively generate the triangle for numRows - 1 and then calculate the 
current row by summing the adjacent elements from the previous row.

Approach 2: Using Combinatorial Formula
Intuition: Pascal's triangle can also be generated using combinatorial formula C(n, k) = C(n-1, k-1) + C(n-1, k), 
where C(n, k) represents the binomial coefficient. We can calculate each element of the triangle using this formula. 
This approach avoids the need for storing the entire triangle in memory, making it memory-efficient.

Approach 3: Using Dynamic Programming with 1D Array
Intuition: We can use a dynamic programming approach with a 1D array to generate Pascal's triangle row by row. 
Instead of maintaining a 2D array, we can use a single array to store the current row and update it as we iterate 
through the rows. This approach reduces space complexity.

Here's a brief outline of each approach:
Recursion Approach:
Base case: If numRows is 1, return [[1]].
Recursively generate the triangle for numRows - 1.
Calculate the current row by summing adjacent elements from the previous row.

Combinatorial Formula Approach:
Use the binomial coefficient formula C(n, k) to calculate each element.
Build the triangle row by row using the formula.

Dynamic Programming with 1D Array:
Initialize a 1D array to store the current row.
Iterate through numRows and update the array for each row.

Complexity:
In terms of time complexity, all three methods have the same overall time complexity of O(numRows^2) because 
we need to generate all the elements of Pascal's triangle. However, in terms of space complexity, Method 3 is 
the most efficient as it uses only O(numRows) space, while the other two methods use O(numRows^2) space due to 
storing the entire triangle or previous rows in recursion.
"""
