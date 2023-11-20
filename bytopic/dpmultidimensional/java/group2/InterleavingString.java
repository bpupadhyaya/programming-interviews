// Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
// An interleaving of two strings s and t is a configuration where s and t are divided into n and m
// substrings respectively, such that:
// s = s1 + s2 + ... + sn
// t = t1 + t2 + ... + tm
// |n - m| <= 1
// The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
// Note: a + b is the concatenation of strings a and b.
// Example:
// Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
// Output: true
// Explanation: One way to obtain s3 is:
// Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
// Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
// Since s3 can be obtained by interleaving s1 and s2, we return true.
//
// Tag: 146/150
// Tag: 97/2927, R582/2936 (overall frequency ranking)

import java.util.Stack;
class InterleavingString {
    public static void main(String...args) {
        String s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac";
        System.out.println("Is interleave? " + isInterleave(s1, s2, s3));
    }

    static boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length())
            return false;

        // Co-ordinates are of the form [i,j], corresonding to the indices in s1 and s2
        Stack<int[]> stack = new Stack<int[]>();
        stack.push(new int[]{0,0});

        boolean[][] visited = new boolean[s1.length() + 1][s2.length() + 1];

        while (!stack.empty()) {
            int[] indices = stack.pop();
            int i = indices[0], j = indices[1];
            visited[i][j] = true;

            // We are at the bottom-rightmost coordinate; we're done.
            if (i == s1.length() && j == s2.length())
                return true;

            // Check if we can increment i (travelling right on the graph)
            if (i < s1.length() && !visited[i+1][j] && s1.charAt(i) == s3.charAt(i+j))
                stack.push(new int[] {i+1, j});

            // Check if we can increment j (travelling down on the graph)
            if (j < s2.length() && !visited[i][j+1] && s2.charAt(j) == s3.charAt(i+j))
                stack.push(new int[] {i, j+1});
        }

        return false;
    }
}
