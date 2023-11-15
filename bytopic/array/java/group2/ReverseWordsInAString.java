// Given an input string s, reverse the order of the words.
// A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
// Return a string of the words in reverse order concatenated by a single space.
// Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only
// have a single space separating the words. Do not include any extra spaces.
// Example:
// Input: s = "  hello world  "
// Output: "world hello"
// Explanation: Your reversed string should not contain leading or trailing spaces.
//
// Tag: 21/150
// Tag: 151/2927, R319/2936 (overall frequency ranking)

class ReverseWordsInAString {
    public static void main(String[] args) {
        String s = "  hello world  ";
        System.out.println("Reversed: " + reverseWords(s));
    }

    static String reverseWords (String s){
        // Trim the input string to remove leading and trailing spaces
        String[] str = s.trim().split("\\s+");

        String out = "";
        // Iterate through the words in reverse order
        for (int i = str.length - 1; i > 0; i--) {
            // Append the current word and a space to the output
            out += str[i] + " ";
        }

        // Append the first word to the output, without trailing space
        return out + str[0];
    }
}

