// A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
// The lengths should not have leading zeros.
// For example, a string such as "substitution" could be abbreviated as (but not limited to):
// "s10n" ("s ubstitutio n")
// "sub4u4" ("sub stit u tion")
// "12" ("substitution")
// "su3i1u2on" ("su bst i t u ti on")
// "substitution" (no substrings replaced)
// The following are not valid abbreviations:
// "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
// "s010n" (has leading zeros)
// "s0ubstitution" (replaces an empty substring)
// Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.
// A substring is a contiguous non-empty sequence of characters within a string.
// Sample 1:
// Input: word = "internationalization", abbr = "i12iz4n"
// Output: true
// Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
// Tag: fb R17/50

class ValidWordAbbreviation {
    public static void main(String...args) {
        String word = "internationalization";
        String abbr = "i12iz4n";
        System.out.println("Valid abbr? " + validWordAbbreviation(word, abbr));
    }

    static boolean validWordAbbreviation(String word, String abbr) {
        if (word == null || abbr == null) {
            throw new IllegalArgumentException("Input is null");
        }
        int wLen = word.length();
        int aLen = abbr.length();
        if (aLen > wLen)
            return false;
        if (wLen == 0)
            return true;

        int i = 0;
        int j = 0;

        while (i < wLen && j < aLen) {
            if (word.charAt(i) == abbr.charAt(j)) {
                i++;
                j++;
                continue;
            }
            if (abbr.charAt(j) == '0' || !Character.isDigit(abbr.charAt(j)))
                return false;


            // The num value
            int num = 0;
            while (j < aLen && Character.isDigit(abbr.charAt(j))) {
                num = 10 * num + (abbr.charAt(j) - '0');
                j++;
            }
            // Increment word pointer by num
            i += num;
        }
        // If both i and j pointers are at end, then we have a valid word abbrevation
        return i == wLen && j == aLen;
    }
}

// Soln:
// TC: O(abbr), SC: O(1)