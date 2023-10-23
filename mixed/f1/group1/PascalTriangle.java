// Given an integer numRows, return the first numRows of Pascal's triangle.
// In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
//           1
//        1     1
//     1    2      1
//  1    3      3     1
// 1  4     6      4    1
// Sample 1:
// Input: numRows = 5
// Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

import java.util.ArrayList;
import java.util.List;
class PascalTriangle {
    public static void main(String...args) {
        int numRows = 5;
        List<List<Integer>> pt = generatePascalTriangle(numRows);
        for (List<Integer> row: pt) {
            System.out.println(row);
        }
    }

    static List<List<Integer>> generatePascalTriangle(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        if (numRows == 0)
            return result;

        if (numRows == 1) {
            List<Integer> firstRow = new ArrayList<>();
            firstRow.add(1);
            result.add(firstRow);
            return result;
        }

        result = generatePascalTriangle(numRows - 1);
        List<Integer> prevRow = result.get(numRows - 2);
        List<Integer> currRow = new ArrayList<>();
        currRow.add(1);

        for (int i = 1; i < numRows - 1; i++) {
            currRow.add(prevRow.get(i-1) + prevRow.get(i));
        }

        currRow.add(1);
        result.add(currRow);

        return result;
    }
}