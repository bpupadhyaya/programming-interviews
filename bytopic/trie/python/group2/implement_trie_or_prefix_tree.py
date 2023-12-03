"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys
in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false
otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has
the prefix prefix, and false otherwise.

Example:
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output:
[null, null, true, false, true, null, true]
Explanation:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   return True
trie.search("app");     return False
trie.startsWith("app"); return True
trie.insert("app");
trie.search("app");     return True

Tag: 98/150
Tag: 208/2927, R672/2936 (overall frequency ranking)
"""


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]
        return '*' in cur

    def starts_with(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]
        return True


def main():
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))         # return True
    print(trie.search("app"))           # return False
    print(trie.starts_with("app"))      # return True
    trie.insert("app")
    print(trie.search("app"))           # return True


if __name__ == "__main__":
    main()
