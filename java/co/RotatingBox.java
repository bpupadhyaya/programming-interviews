// Given a matrix, m x n, of characters representing a side of a box, each cell being one of the following:
// a stone (#), a stiationary obstacle (*), or empty (.). Find an n x m matrix representing the rotated box.
// Additional info: box is rotated 90 degrees clockwise, which causes some of the stones to fall due to gravity.
// Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity has no
// effect on obstacles' positions. Box inertia due to rotation does not affect the stones' horizontal positions.
// It is assumed that each stone in the box rests on an obstacle, another stone, or the bottom of the box.
// Sample Input and output:
// input: [['#','.','*','.']
//          ['#','#','*','.']]
// output: [ ['#','.']
//           ['#','#']
//           ['*','*']
//           ['.','.']]

class RotatingBox {
    public static void main(String[] args) {
        char[][] input = {{'#','.','*','.'},{'#','#','*','.'}};
        char[][] output = rotateBox(input);
        for (int i = 0; i < output.length; i++) {
            for (int j = 0; j < output[0].length; j++) {
                System.out.print(output[i][j]+",");
            }
            System.out.println();
        }
        System.out.println();
    }

    private static char[][] rotateBox(char[][] box) {
        for (int i = 0; i < box.length; i++) {
            Integer le = null;
            for(int j = box[0].length - 1; j >= 0; j--)
                if(le == null && box[i][j] == '.')
                    le = j;
                else if(box[i][j] == '#' && le != null) {
                    box[i][j] = '.';
                    box[i][le--] = '#';
                } else if (box[i][j] == '*')
                    le = null;
        }

        char[][] result = new char[box[0].length][box.length];
        for (int i = 0; i < box.length; i++)
            for(int j = box[0].length - 1; j >= 0; j--)
                result[j][box.length - i - 1] = box[i][j];
        return result;
    }

}