// Given an m x n board of characters and a list of strings words, return all words on the board.
// Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
// or vertically neighboring. The same letter cell may not be used more than once in a word.
// Example:
// Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
// words = ["oath","pea","eat","rain"]
// Output: ["eat","oath"]
// Note: Visualize to understand
//
// Tag: 100/150
// Tag: 212/2927, R469/2936 (overall frequency ranking)

import java.util.ArrayList;
import java.util.List;

class TrieNode {
    TrieNode[] next = new TrieNode[26];
    String word;
}
class WordSearchII {
    public static void main(String...args) {
        char[][] board = {
                {'o','a','a','n'},
                {'e','t','a','e'},
                {'i','h','k','r'},
                {'i','f','l','v'}
        };
        String[] words = {"oath","pea","eat","rain"};

        List<String> result = findWords(board, words);
        System.out.println("Result: " + result);
    }

    static List<String> findWords(char[][] board, String[] words) {
        List<String> res = new ArrayList<>();
        TrieNode root = buildTrie(words);
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                dfs(board, i, j, root, res);
            }
        }
        return res;
    }

    private static void dfs(char[][] board, int i, int j, TrieNode p, List<String> res) {
        char c = board[i][j];
        if (c == '#' || p.next[c - 'a'] == null)
            return;
        p = p.next[c - 'a'];
        if (p.word != null) { // found
            res.add(p.word);
            p.word = null; // de-duplciate
        }

        board[i][j] = '#';
        if (i > 0) dfs(board, i-1, j, p, res);
        if (j > 0) dfs(board, i, j-1, p, res);
        if (i < board.length - 1) dfs(board, i+1, j, p, res);
        if (j < board[0].length -1) dfs(board, i, j+1, p, res);
        board[i][j] = c;
    }

    private static TrieNode buildTrie(String[] words) {
        TrieNode root = new TrieNode();
        for (String w: words) {
            TrieNode p = root;
            for (char c: w.toCharArray()) {
                int i = c - 'a';
                if (p.next[i] == null)
                    p.next[i] = new TrieNode();
                p = p.next[i];
            }
            p.word = w;
        }
        return root;
    }
}
