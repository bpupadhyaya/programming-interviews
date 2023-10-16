// Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where
// each word is a valid dictionary word. Return all such possible sentence in any order.
// Note that the same word in the dictinary may be reused multiple times in the segmentation.
// Sample 1:
// Input: s = "mangoandorange", wordDict = ["man", "mango", "go", "and", "orange"]
// Output: ["mango and orange", "man go and orange"]

import java.util.List;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;
class WordBreak {
    public static void main(String...args) {
        String myString = "mangoandorange";
        String[] wordDictArr = {"man", "mango", "go", "and", "orange"};;
        Set<String> wordDictSet = new HashSet<>(Arrays.asList(wordDictArr));
        List<String> sentences = findSentences(myString, wordDictSet);
        for (String sentence: sentences) {
            System.out.println("Sentence: " + sentence);
        }

    }

    static List<String>  findSentences(String s, Set<String> wordDict) {
        HashMap<String, LinkedList<String>> myMap = new HashMap<String, LinkedList<String>>();

        return workBreakDFS(s, wordDict, myMap);
    }

    static List<String> workBreakDFS(String s, Set<String> wordDict, HashMap<String, LinkedList<String>> myMap) {
        if (myMap.containsKey(s))
            return myMap.get(s);

        LinkedList<String> result = new LinkedList<String>();
        if (s.length() == 0) {
            result.add("");
            return result;
        }

        for (String word: wordDict) {
            if (s.startsWith(word)) {
                List<String> subList = workBreakDFS(s.substring(word.length()), wordDict, myMap);
                for (String sub: subList)
                    result.add(word + (sub.isEmpty()? "": " ") + sub);
            }
        }
        myMap.put(s, result);

        return result;
    }
}