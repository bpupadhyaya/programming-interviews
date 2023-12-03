"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Tag: 97/150
Tag: 127/2927, R326/2936 (overall frequency ranking)
"""
from collections import defaultdict
from collections import deque


def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    if end_word not in word_list or not end_word or not begin_word or not word_list:
        return 0
    beg_len = len(begin_word)
    all_combo_dict = defaultdict(list)
    for word in word_list:
        for i in range(beg_len):
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
    queue = deque([(begin_word, 1)])
    visited = set()
    visited.add(begin_word)
    while queue:
        current_word, level = queue.popleft()
        for i in range(beg_len):
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            for word in all_combo_dict[intermediate_word]:
                if word == end_word:
                    return level + 1
                if word not in visited:
                    visited.add(word)
                    queue.append((word, level + 1))
    return 0


def main():
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(ladder_length(begin_word, end_word, word_list))


if __name__ == "__main__":
    main()
