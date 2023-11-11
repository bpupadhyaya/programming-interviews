// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if
// needle is not part of haystack.
// Example:
// Input: haystack = "sadbutsad", needle = "sad"
// Output: 0
// Explanation: "sad" occurs at index 0 and 6.
// The first occurrence is at index 0, so we return 0.
// Tag: 23/150

class FindingTheIndexOfTheFirstOccurrenceInAString {
    public static void main(String...args) {
        String haystack = "sadbutsad";
        String needle = "sad";
        System.out.println("Index: " + findNeedleInHaystack(haystack, needle));
    }

    static int findNeedleInHaystack(String haystack, String needle) {
        for (int i = 0; ; i++) {
            for (int j = 0; ; j++) {
                if (j == needle.length()) return i;
                if (i + j == haystack.length()) return -1;
                if (needle.charAt(j) != haystack.charAt(i+j)) break;
            }
        }
    }
}