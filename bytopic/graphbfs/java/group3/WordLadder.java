// A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
// beginWord -> s1 -> s2 -> ... -> sk such that:
// - Every adjacent pair of words differs by a single letter.
// - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
// - sk == endWord
// Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
// transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
// Example:
// Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
// Output: 5
// Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
//
// Tag: 97/150
// Tag: 127/2927, R326/2936 (overall frequency ranking)

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.List;

class WordLadder {
    public static void main(String...args) {
       String beginWord = "hit";
       String endWord = "cog";
       String[] wordListArray = {"hot","dot","dog","lot","log","cog"};
       List<String> wordList = Arrays.asList(wordListArray);
       System.out.println("Num. of words in shortest...: " + ladderLength(beginWord, endWord, wordList));
    }

    static int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> beginSet = new HashSet<String>(), endSet = new HashSet<String>();

        int len = 1;
        int strLen = beginWord.length();
        HashSet<String> visited = new HashSet<String>();

        beginSet.add(beginWord);
        endSet.add(endWord);
        while (!beginSet.isEmpty() && !endSet.isEmpty()) {
            if (beginSet.size() > endSet.size()) {
                Set<String> set = beginSet;
                beginSet = endSet;
                endSet = set;
            }

            Set<String> temp = new HashSet<String>();
            for (String word: beginSet) {
                char[] chs = word.toCharArray();

                for (int i = 0; i < chs.length; i++) {
                    for (char c = 'a'; c <= 'z'; c++) {
                        char old = chs[i];
                        chs[i] = c;
                        String target = String.valueOf(chs);

                        if (endSet.contains(target)) {
                            return len + 1;
                        }

                        if (!visited.contains(target) && wordList.contains(target)) {
                            temp.add(target);
                            visited.add(target);
                        }
                        chs[i] = old;
                    }
                }
            }
            beginSet = temp;
            len++;
        }

        return 0;
    }
}