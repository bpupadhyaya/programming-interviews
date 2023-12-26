"""
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings
in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of
letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically
 increasing order by the new language's rules. If there are multiple solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

R116/145
"""
from collections import defaultdict
from typing import Dict, Set


def alien_order(words: list[str]) -> str:
    # These are the unique letters in the list of words
    charset = set(''.join(words))

    def build_graph(words: list[str]) -> (Dict[str, list[str]], Dict[str, int]):
        # defaultdict works great in this case, because we don't have to initialize the list
        # NOTE that we can't relay on it to have a complete set of all possible characters,
        # we use the character set instead
        graph = defaultdict(list)
        # This defultdict is used to keep track of the number of edges going into a node
        # later on, we will use it to ensure that these nodes are visited in the correct order
        # and detect circular dependencies
        indegree = defaultdict(int)
        # Zip creates an iterator of tuples from the given lists.  The tuples are groups of elements
        # by index, that is why the second argument is a slice of the words list starting at 1.
        # if words = ['aa', 'bb', 'cc']
        #  zip(words, words[1:])  =  zip(['aa', 'bb', 'cc'], ['bb', 'cc'])
        # the result will be an iterator equivalent to [('aa', 'bb'), ('bb', 'cc')]
        for word1, word2 in zip(words, words[1:]):
            # Note that by using zip here, will save us the trouble of having to
            # find out which of the two words is the shortest. We are only guaranteed
            # lexicographical order up to the first character that is different or to the
            # length of the shortest word. Think of the words:
            #  acid
            #  acidize
            # Here we can only compare up to the length of the shortest word
            #
            # OR
            #  aaz
            #  aba
            #
            # Here we can only compare up to the first group of characters that do not match ('a', 'b') at index 1
            # anything else beyond these two conditions may have any character.
            for char1, char2 in zip(word1, word2):
                # Ignore all characters that are equal as these are not relevant; continue to
                # iterate until the first group of characters that do not match
                if char1 != char2:
                    # char1 is the node and char2 is adjacent to it, so it is added to its adjacency list
                    # aka neighbors/children
                    graph[char1].append(char2)
                    # Record that the char2 has an incoming edge
                    indegree[char2] += 1
                    break
        return graph, indegree

    def bfs(graph: Dict[str, list[str]], indegree: Dict[str, int], charset: Set[str]) -> str:
        # Add all the characters that don't have any incoming edges to the queue
        queue = [char for char in charset if indegree[char] == 0]
        result = ''
        while queue:
            # Pop an element from the queue and assign it to cur/current and append it to the result
            cur = queue.pop()
            result += cur
            # Iterate over the list of children, this is the list of nodes adjacent to the current one
            for child in graph[cur]:
                # A completely disconnected circular dependency e.g. a -> b -> a will never end up in the queue
                # A circular dependency that is connected to more than one node will have an in-degree greater
                # than 1 e.g. r -> x -> q -> j -> d -> j
                #                            |--> f -> o
                # In this graph, j has an in-degree of 2 and it will never make it to the queue
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.insert(0, child)
        # In the end, the result will be the letters organized in topological order if
        # result contains the same number of letters as the charset if it contains
        # fewer letters than the charset it means we have detected a circular dependency
        # and should return an empty string.
        return result if len(result) == len(charset) else ''

    graph, indegree = build_graph(words)
    return bfs(graph, indegree, charset)


def main():
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print(alien_order(words))


if __name__ == "__main__":
    main()
