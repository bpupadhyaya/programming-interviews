"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

Tag: R54/145
"""


def word_break(s: str, word_dict: list[str]) -> bool:
    def construct(current, word_dict, memo={}):
        if current in memo:
            return memo[current]
        if not current:
            return True
        for word in word_dict:
            if current.startswith(word):
                new_current = current[len(word):]
                if construct(new_current, word_dict, memo):
                    memo[current] = True
                    return True
        memo[current] = False
        return False
    return construct(s, word_dict)


def word_break_1(s: str, word_dict: list[str]) -> bool:
    # DP
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True
    max_len = max(map(len, word_dict))  # The maximum length of a word in the dictionary
    for i in range(1, n+1):
        for j in range(i-1, max(i - max_len - 1, -1), -1): # Only consider words that could fit
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[n]


def word_break_2(s: str, word_dict: list[str]) -> bool:
    # Depth first search with memoization
    memo = {}
    word_set = set(word_dict)

    def dfs(s, word_set, memo):
        if s in memo:
            return memo[s]
        if s in word_set:
            return True
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix in word_set and dfs(s[i:], word_set, memo):
                memo[s] = True
                return True
        memo[s] = False
        return False
    return dfs(s, word_set, memo)


def main():
    s = "applepenapple"
    word_dict = ["apple", "pen"]
    print(word_break_2(s, word_dict))


if __name__ == "__main__":
    main()

"""
Dynamic Programming
By utilizing a boolean array dp, we can iteratively build a solution that checks if the string can be segmented 
into dictionary words. This approach leverages the subproblem overlap and builds a bottom-up solution.

Depth-First Search with Memoization
This approach searches for a valid segmentation by recursively exploring different paths and using a set data 
structure to efficiently match prefixes. Memoization is used to store results and avoid redundant computations.

Differences
While Dynamic Programming builds the solution iteratively, Depth-First Search explores recursively. The DP approach 
has a more straightforward implementation, while DFS with memoization may be more efficient in some cases due to 
early termination.

Approach - Dynamic Programming
The Dynamic Programming approach provides an efficient way to solve the word break problem by building up a 
solution iteratively. Here's a step-by-step description:

Initialization: We initialize a boolean array dp of length (n+1), where (n) is the length of the string s. The 
entry dp[i] will be True if there exists a word in the dictionary that ends at index (i-1) in the string s. 
We set dp[0] to True since an empty string can always be segmented.

Determine Maximum Word Length: We find the maximum length of a word in the dictionary using 
max_len = max(map(len, wordDict)). This helps us in reducing unnecessary iterations.

Iterate Through the String: We iterate through the string from index 1 to (n) (inclusive) and for each index i, 
we iterate from index (i-1) down to (i - max_len - 1) (or -1, whichever is larger).

Check for Segmentation: For each j in the range, we check if dp[j] is True and if the substring s[j:i] is in 
wordDict. If both conditions are met, we set dp[i] to True and break out of the inner loop. This means that 
there exists a valid segmentation ending at index (i-1).

Result: Finally, we return dp[n], which will be True if the entire string can be segmented into words from 
the dictionary.

Example:
Consider the example with s = "leetcode" and wordDict = ["leet","code"]. Here's how the algorithm proceeds:

Initialization: dp = [True, False, False, False, False, False, False, False, False].
Determine Maximum Word Length: max_len = 4.
Iterate Through the String:
When i = 4, the loop finds that dp[0] is True and "leet" is in the dictionary, so dp[4] is set to True.
When i = 8, the loop finds that dp[4] is True and "code" is in the dictionary, so dp[8] is set to True.
Result: dp[8] is True, so the function returns True.
The use of dynamic programming ensures that we are not recomputing solutions to subproblems, and the 
consideration of the maximum word length helps in avoiding unnecessary iterations, making this approach both 
elegant and efficient.

Complexity
Time complexity: ( O(n * m) ), where ( n ) is the length of the string and ( m ) is the maximum length of a word 
in the dictionary.
Space complexity: ( O(n) )


Depth-First Search with Memoization:
The Depth-First Search (DFS) approach with memoization offers a recursive way to solve the word break problem. 
It leverages the Trie data structure to efficiently match prefixes and employs memoization to 
store intermediate results. Here's a step-by-step description:

Building the Trie: We initialize an empty Trie and iterate through each word in the dictionary (wordDict). 
For each word, we add it to the Trie, using a nested loop to traverse each character (ch) in the word. We 
use the '#' symbol to mark the end of a word in the Trie. We also determine the maximum length (max_len) of a word 
in the dictionary.

Initialization of Memoization: We initialize an empty dictionary (memo) to store the results of subproblems. 
This helps in avoiding redundant computations.

DFS Function Call: We call the recursive DFS function with initial parameters, starting from index 0.

Recursive DFS Function:

Memoization Check: If the starting index (start) is found in memo, we return the stored result.
Base Case: If start equals the length of the string, we return True, as we have reached the end.
Iterate Through Prefixes: We initialize node to the root of the Trie and iterate through the string from the 
start index to the minimum of start + max_len and the length of the string.
Trie Traversal: For each character (ch), we traverse the Trie. If ch is not found, we break out of the loop.
Check for Word End and Recursion: If we find the end of a word marker ('#') in the Trie, we make a recursive call 
to dfs with the next index (i + 1).
Update Memoization: If the recursive call returns True, we update memo[start] to True and return True.
Result: Finally, we update memo[start] to False if no valid segmentation is found and return False.

This approach leverages the Trie structure to efficiently match prefixes and uses memoization to enhance efficiency. 
It offers a recursive and elegant solution to the word break problem.

Complexity
Time complexity: ( O(n * m + k) ), where ( n ) is the length of the string, ( m ) is the maximum length of a word 
in the dictionary, and ( k ) is the total number of characters in all words in the dictionary (for building the Trie).
Space complexity: ( O(n + k) ), where ( n ) is the length of the string and ( k ) is the total number of characters 
in all words in the dictionary.

"""
