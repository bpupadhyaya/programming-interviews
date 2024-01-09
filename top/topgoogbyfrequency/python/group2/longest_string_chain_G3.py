"""
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing
the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2,
word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.

"""


def longest_str_chain(words: list[str]) -> int:
    # Recursive (top-down)
    chain_lengths = {}
    word_set = {}

    def calculate_chain_length(word_) -> int:
        # If the word doesn't exist in the set
        if word_ not in word_set or not word_set[word_]:
            return 0

        # If chain length for the word is already calculated
        if word_ in chain_lengths:
            return chain_lengths[word_]

        chain_length = 1

        # Try removing one character at a time from the word and calculate chain length
        for i in range(len(word_)):
            new_word = word_[:i] + word_[i + 1:]
            chain_length = max(chain_length, 1 + calculate_chain_length(new_word))

        chain_lengths[word_] = chain_length
        return chain_length

    for word in words:
        word_set[word] = True

    max_chain_length = -1

    # Calculate the maximum chain length for each word
    for word in words:
        max_chain_length = max(max_chain_length, calculate_chain_length(word))

    return max_chain_length


def longest_str_chain1(words: list[str]) -> int:
    # Iterative (bottom up)
    # Sort the words by their lengths
    words.sort(key=len)

    # Dictionary to store the longest chain length for each word
    longest_chain_length = {}

    # Initialize the answer
    max_chain_length = -1

    for word in words:
        # Initialize the chain length for the current word
        longest_chain_length[word] = 1

        # Try removing one character at a time from the word and check if the resulting word exists
        for i in range(len(word)):
            reduced_word = word[:i] + word[i + 1:]

            # If the reduced word exists in the dictionary
            if reduced_word in longest_chain_length:
                # Update the chain length for the current word
                longest_chain_length[word] = max(longest_chain_length[word], longest_chain_length[reduced_word] + 1)

        # Update the maximum chain length seen so far
        max_chain_length = max(max_chain_length, longest_chain_length[word])

    return max_chain_length


def longest_str_chain2(words: list[str]) -> int:
    # dp
    words.sort(key=len)
    dp = {}
    max_chain = 0
    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            prev_word = word[:i] + word[i+1:]
            if prev_word in dp:
                dp[word] = max(dp[word], dp[prev_word] + 1)
        max_chain = max(max_chain, dp[word])
    return max_chain


def longest_str_chain3(words: list[str]) -> int:
    # Memoization
    word_set = set(words)
    memo = {}

    def dfs(word):
        if word not in word_set:
            return 0

        if word in memo:
            return memo[word]

        max_chain = 1
        for i in range(len(word)):
            next_word = word[:i] + word[i+1:]
            max_chain = max(max_chain, 1 + dfs(next_word))

        memo[word] = max_chain
        return max_chain

    return max(dfs(word) for word in words)


def main():
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    print(longest_str_chain3(words))


if __name__ == "__main__":
    main()

"""
Recursive Approach (Top-Down)
Approach
Create two empty dictionaries: chain_lengths to store chain lengths (DP) and word_set to track word existence.
Calculate Chain Length:
If the word is not in word_set, return 0 (word doesn't exist in the set).
If the chain length for the word is already calculated, return the stored chain length (DP).
Iterate through each character in the word:
Create a new word by removing the current character.
Recur and calculate chain length for the new word.
Update chain_length.
Return the final chain_length.
Longest Word Chain:
Add the word to the word_set and mark it as existing.
Initialize max_chain_length to -1 (no chain found yet).
Iterate through each word in the input list:
Calculate the chain length for the current word.
Update max_chain_length.
Return the final max_chain_length.
Complexity
Time complexity: O(N∗M)
Since we are iterating over all the N words and in each word we try all possible predecessor by removing one 
character a time then the time complexity is O(N * M).
Where N is the number of words in our array and M is the length of the word.
remember that we eliminated redundant calls by using DP.
Space complexity: O(N)
We store two HashMaps each of size N then the space we are storing is 2 * N then the space complexity it O(N).

Iterative Approach (Bottom-Up)
Approach
Sort the words in the input vector based on their lengths in ascending order.
Initialize a map called longestChainLength to store the longest chain length for each word.
Initialize a variable maxChainLength to -1 to (no chain found yet).
Iterate through each word in the sorted list of words:
Initialize the chain length for the current word as 1 (The word itself).
remove one character at a time and check if the resulting word exists.
If the resulted word exists in the map:
Update the chain length.
Update the maximum chain length seen so far.
Return Maximum Chain Length.
Complexity
Time complexity: O(N∗(log(N)+M))
Since we are sorting the array of words then iterating over all the N words and in each word we try all possible
 predecessor by removing one character a time then the time complexity is O(N * log(N) + N * M).
Where N is the number of words in our array and M is the length of the word.
remember that we eliminated redundant calls by using DP;`
Space complexity: O(N)
We store one HashMaps of size N then the space we are storing is N then the space complexity it O(N).

DP explanation:
Dynamic Programming
Tackling the "Longest String Chain" puzzle requires a blend of systematic organization and methodical computation. 
Our primary weapon of choice for this challenge is Dynamic Programming, a strategy that breaks problems down into 
smaller, more manageable sub-problems. The beauty of this approach lies in its ability to remember past results, 
which significantly speeds up computing the final solution.

Key Data Structures:
dp: A dictionary, acting like our memory vault, that remembers the longest chain length we can achieve for each word.
Detailed Breakdown:
Setting the Stage - Organizing Words:

Imagine you're arranging dominoes; the smallest pieces first, growing to the largest. Similarly, we start by 
sorting our words from shortest to longest. This ensures that when we're looking at a word, any 
potential 'parent' word (a word it could have evolved from) has already been evaluated.
Constructing Chains:

For every word, we assume it to be a unique entity and assign a chain length of 1. This is our base scenario, 
the minimal chain.
Now, we dive deep into each word. By omitting one character at a time, we attempt to form a predecessor word.
 If this predecessor exists in our dp (our memory vault), it means our current word could have evolved from it. 
 Using the transition function, we then update our current word's chain length based on the predecessor's length.
Why the Transition Function?
In dynamic programming, transition functions act like bridges, connecting sub-problems to construct the bigger
 picture. Here, it helps us decide if the chain length of the current word should be updated based on its 
 predecessor. It's the heart of our solution, ensuring we always have the longest chain possible.

Complexity Commentary:
Time Complexity:

Our method involves scanning through our sorted list of words. For each word, it evaluates all possible words 
it could have evolved from. This double traversal gives rise to a time complexity of O(n×m), 
where nnn denotes the total number of words and mmm signifies the average word length.
Space Complexity:

Our dp dictionary occupies space based on the number of words, giving us a space complexity of O(n).

Memoization explanation:
Memoization with DFS Approach:
This approach uses DFS to explore the potential chains starting from each word. To optimize the solution, 
the results of expensive recursive calls are cached using memoization.

Key Data Structures:
memo: A dictionary to cache the results of DFS calls for each word.
Enhanced Breakdown:
DFS Exploration:

For each word, recursively explore its potential predecessors by removing one character at a time.
Cache the result of the DFS exploration for each word to avoid redundant calculations.
Check Maximum Chain Length:

After exploring all potential chains starting from a word, store the maximum chain length found in the memo dictionary.
Complexity Analysis:
Time Complexity:

The algorithm explores each word once and, for each word, checks all its potential predecessors. Due to memoization,
 repeated calculations are avoided. The time complexity is O(n×m).
Space Complexity:

The space complexity is O(n) due to the storage requirements of the memo dictionary and the word_set.

"""