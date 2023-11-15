// Given a string s consisting of words and spaces, return the length of the last word in the string.
// A word is a maximal substring consisting of non-space characters only.
// Input: s = "   fly me   to   the moon  "
// Output: 4
// Explanation: The last word is "moon" with length 4.
//
// Tag: 19/150
// Tag: 58/2927, R712/2936 (overall frequency ranking)

class LengthOfLastWord {
    public static void main(String...args) {
        String s = "   fly me   to   the moon  ";
        System.out.println("Length of last word: " + lengthOfLastWord(s));
    }

    static int lengthOfLastWord(String s) {
        int length = 0;
        // We are looking for the last word, so can go backward
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) != ' ') { // A letter is found so count
                length++;
            } else { // It is a white space
                // Did we already start to cont a word? If yes, we found the last word
                if (length > 0) return length;
            }
        }
        return length;
    }
}