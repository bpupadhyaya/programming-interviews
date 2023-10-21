// You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
// DO NOT allocate another 2D matrix and do the rotation.
// Note: visualize in order understand
// Sample 1
// Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [[7,4,1],[8,5,2],[9,6,3]]

class RotateImage {
    public static void main(String...args) {
        int[][] mat = {
                {1,2,3},
                {4,5,6},
                {7,8,9}
        };

        System.out.println("Rotated: ");
        rotateImage(mat);
        for(int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat.length; j++) {
                System.out.print(mat[i][j]+", ");
            }
            System.out.println();
        }

    }

    static void rotateImage(int[][] mat) {
        int n = mat.length, depth = n / 2;
        for (int i = 0; i < depth; i++) {
            int len = n -2 * i -1, opp = n - 1 - i;
            for (int j = 0; j < len; j++) {
                int temp = mat[i][i+j];
                mat[i][i+j] =  mat[opp-j][i];
                mat[opp-j][i] = mat[opp][opp-j];
                mat[opp][opp-j] = mat[i+j][opp];
                mat[i+j][opp] = temp;
            }
        }
    }
}