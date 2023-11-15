// Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and
// is fully (left and right) justified.
// You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when
// necessary so that each line has exactly maxWidth characters.
// Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide
// evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
// For the last line of text, it should be left-justified, and no extra space is inserted between words.
// Note:
// A word is defined as a character sequence consisting of non-space characters only.
// Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
// The input array words contains at least one word.
// Example:
// Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
// Output:
// [
//    "This    is    an",
//    "example  of text",
//    "justification.  "
// ]
//
// Tag: 24/150
// Tag: 68/2927, R50/2936 (overall frequency ranking)

import java.util.ArrayList;
import java.util.List;
class TextJustification {
    public static void main(String[] args) {
        String[] words = {"This", "is", "an", "example", "of", "text", "justification."};
        int maxWidth = 16;
        List<String> result = fullJustify(words, maxWidth);
        for (String elem: result)
            System.out.println(elem);
    }

    static List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList<>();
        List<String> cur = new ArrayList<>();
        int numOfLetters = 0;

        for (String word: words) {
            if (word.length() + cur.size() + numOfLetters > maxWidth) {
                for (int i = 0; i < maxWidth - numOfLetters; i++) {
                    cur.set(i % (cur.size() - 1 > 0 ? cur.size() - 1 : 1), cur.get(i % (cur.size() - 1 > 0 ? cur.size() - 1 : 1)) + " ");
                }
                StringBuilder sb = new StringBuilder();
                for (String s: cur) sb.append(s);
                res.add(sb.toString());
                cur.clear();
                numOfLetters = 0;
            }
            cur.add(word);
            numOfLetters += word.length();
        }

        StringBuilder lastLine = new StringBuilder();
        for (int i = 0; i < cur.size(); i++) {
            lastLine.append(cur.get(i));
            if (i != cur.size() - 1) lastLine.append(" ");
        }
        while (lastLine.length() < maxWidth) lastLine.append(" ");
        res.add(lastLine.toString());

        return res;
    }
}

// Logic : Modulo-based Space Distribution
// To solve the "Text Justification" problem using this approach, we pack words into each line using a greedy strategy.
// We then distribute spaces among the words on each line, using modulo arithmetic to decide where to place the extra spaces.
//
// Key Data Structures:
// List: To store the current words for a line and the result.
//
// Steps:
// 1. Initialization:
// -We start by initializing empty lists for the result and the current line words.
// -A counter is also initialized to keep track of the total length of words in the current line.
// 2. Processing Each Word:
// -For each word, we check if adding the next word to the current line would make it exceed the maximum width.
// -If it does, we proceed to justify the current line. This involves distributing spaces among the words. The modulo arithmetic
// is handy here, ensuring that extra spaces are evenly spread among the words.
// -Once the line is justified, we reset the lists and counter for the next line.
// -A special case is the last line, where we simply left-justify the words.
// 3. Wrap-up:
// Once all the words are processed and lines are justified, we return the result list.
//
// Example:
// Given the words = ["This", "is", "an", "example"] and maxWidth = 16:
// The word "This" is added to the current line.
// The word "is" is added to the current line.
// The word "an" is added to the current line, completing it with the string "This is an".
// The word "example" starts a new line.
// Complexity:
// Time Complexity ~ O(n), where n is the number of words.
// Space Complexity ~ O(n×m), where n is the number of words and m is the average length of the words.