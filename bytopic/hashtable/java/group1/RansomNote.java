// Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the
// letters from magazine and false otherwise.
// Each letter in magazine can only be used once in ransomNote.
// Example 1:
// Input: ransomNote = "aa", magazine = "aab"
// Output: true
// Example 2:
// Input: ransomNote = "aa", magazine = "ab"
// Output: false
// Tag: 39/150

class RansomNote {
    public static void main(String[] args) {
        String ransomNote = "aa";
        String magazine = "aab";
        System.out.println("Can construct? " + canConstruct(ransomNote, magazine));
    }

    static boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() > magazine.length()) return false;
        int[] alphabetsCounter = new int[26];

        for (char c: magazine.toCharArray())
            alphabetsCounter[c - 'a']++;

        for (char c: ransomNote.toCharArray()) {
            if (alphabetsCounter[c - 'a'] == 0) return false;
            alphabetsCounter[c - 'a']--;
        }

        return true;
    }
}