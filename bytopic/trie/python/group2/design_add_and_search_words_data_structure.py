"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.

Example:
Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output:
[null,null,null,null,false,true,true,true]

Tag: 99/150
Tag: 211/2927, R1021/2936 (overall frequency ranking)
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        current_node = self.root
        for character in word:
            current_node = current_node.children.setdefault(character, TrieNode())
        current_node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_word
            if word[index] == '.':
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)
            return False
        return dfs(self.root, 0)


def main():
    word_dictionary = WordDictionary()
    word_dictionary.add_word("dad")
    word_dictionary.add_word("mad")
    word_dictionary.add_word("bad")
    print(word_dictionary.search("dad"))
    print(word_dictionary.search("cat"))


if __name__ == "__main__":
    main()
