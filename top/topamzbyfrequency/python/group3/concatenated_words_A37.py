"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words
(not necessarily distinct) in the given array.

Example:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Tag: 472/2927 , R1070/2935 , R37/50 (amz)
Note: Output characters, in the first implementation, are correct, but they are not grouped in words, debug and fix.
Second implementation works.
"""
import collections
import functools


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        marker = self.root
        for ch in word:
            marker = marker.children[ch]
        marker.isEnd = True


def find_all_concatenated_words_in_a_dict(words: list[str]) -> list[str]:
    def dfs(word_, start, root, count):
        n = len(word_)
        marker = root
        for i in range(start, n):
            marker = marker.children[word_[i]]
            if marker.isEnd:        # smaller word encountered
                if i == n - 1:
                    return count >= 1
                elif dfs(word_, i + 1, root, count + 1):  # increment the count and start a new DFS
                    return True
        return False

    res = []
    trie = Trie()
    for word in words:
        trie.insert(word)

    for word in words:
        if dfs(word, 0, trie.root, 0):
            res += word

    return res


def find_all_concatenated_words_in_a_dict_1(words: list[str]) -> list[str]:
    # Create a set of all words in the given list
    word_set = set(words)

    # Define a recursive function to check if a word is concatenated
    @functools.lru_cache(None)  # Memoize the function with least-recently-used cache
    def is_concat(word: str) -> bool:
        for i in range(1, len(word)):  # Try all possible splits of the word
            prefix = word[:i]  # Get the prefix of the split
            suffix = word[i:]  # Get the suffix of the split
            if prefix in word_set and (suffix in word_set or is_concat(suffix)):
                # If the prefix is in the word_set and the suffix is either in the word_set
                # or can be formed by concatenating other words, then the word is
                # concatenated
                return True
        return False

    # Use a list comprehension to get all concatenated words
    return [word for word in words if is_concat(word)]


def main():
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    print(find_all_concatenated_words_in_a_dict_1(words))


if __name__ == "__main__":
    main()


"""
Steps:
1. Create a set of all words in the given list.
2. Define a recursive function called isConcat to check if a word is concatenated.
3. Memoize the isConcat function using the functools.lru_cache decorator to cache its results and improve performance.
4. For a given word, try all possible splits of the word by iterating over its characters using a for loop.
5. For each split, get the prefix and suffix of the split using string slicing.
6. Check if the prefix is in the wordSet.
7. If the prefix is in the wordSet, check if the suffix is either in the wordSet or can be formed by concatenating 
  other words by recursively calling the isConcat function on the suffix.
8. If the suffix is either in the wordSet or can be formed by concatenating other words, then the word is concatenated 
  and we can return True from the isConcat function.
9. If none of the splits result in a concatenated word, then the word is not concatenated and we can return False from 
  the isConcat function.
10. Use a list comprehension to get all concatenated words by iterating over the words in the input list and calling 
  the isConcat function on each word.
11. Return the list of concatenated words.
"""
