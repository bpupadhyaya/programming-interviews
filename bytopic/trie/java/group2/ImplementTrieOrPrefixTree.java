// A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys
// in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
// Implement the Trie class:
// - Trie() Initializes the trie object.
// - void insert(String word) Inserts the string word into the trie.
// - boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false
// otherwise.
// - boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix,
// and false otherwise.
// Example:
// Input:
// ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
// [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
// Output:
// [null, null, true, false, true, null, true]
// Explanation:
// Trie trie = new Trie();
// trie.insert("apple");
// trie.search("apple");   // return True
// trie.search("app");     // return False
// trie.startsWith("app"); // return True
// trie.insert("app");
// trie.search("app");     // return True
//
// Tag: 98/150
// Tag: 208/2927, R672/2936 (overall frequency ranking)

class TrieNode {
    char val;
    boolean isWord;
    TrieNode[] children = new TrieNode[26];
    TrieNode() {}
    TrieNode(char c) {
        TrieNode node = new TrieNode();
        node.val = c;
    }
}
class Trie {
    private TrieNode root;
    public Trie() {
        root = new TrieNode();
        root.val = ' ';
    }

    public void insert(String word) {
        TrieNode ws = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (ws.children[c - 'a'] == null) {
                ws.children[c - 'a'] = new TrieNode(c);
            }
            ws = ws.children[c - 'a'];
        }
        ws.isWord = true;
    }

    public boolean search(String word) {
        TrieNode ws = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (ws.children[c - 'a'] == null)
                return false;
            ws = ws.children[c - 'a'];
        }

        return ws.isWord;
    }

    public boolean startsWith(String prefix) {
        TrieNode ws = root;
        for (int i = 0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);
            if (ws.children[c - 'a'] == null)
                return false;
            ws = ws.children[c - 'a'];
        }

        return true;
    }
}
class TrieOrPrefixTreeImplementation {
    public static void main(String...args) {
        Trie trie = new Trie();
        trie.insert("apple");
        System.out.println(trie.search("apple"));   // return True
        System.out.println(trie.search("app"));     // return False
        System.out.println(trie.startsWith("app")); // return True
        trie.insert("app");
        System.out.println(trie.search("app"));     // return True
    }
}
