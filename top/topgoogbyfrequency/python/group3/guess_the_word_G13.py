"""
You are given an array of unique strings words where words[i] is six letters long. One word of words was chosen
as a secret word.

You are also given the helper object Master. You may call Master.guess(word) where word is a six-letter-long string,
 and it must be from words. Master.guess(word) returns:

-1 if word is not from words, or
an integer representing the number of exact matches (value and position) of your guess to the secret word.
There is a parameter allowedGuesses for each test case where allowedGuesses is the maximum number of times you can
 call Master.guess(word).

For each test case, you should call Master.guess with the secret word without exceeding the maximum number of allowed
 guesses. You will get:

"Either you took too many guesses, or you did not find the secret word." if you called Master.guess more than
 allowedGuesses times or if you did not call Master.guess with the secret word, or
"You guessed the secret word correctly." if you called Master.guess with the secret word with the number of calls
 to Master.guess less than or equal to allowedGuesses.
The test cases are generated such that you can guess the secret word with a reasonable strategy (other than using
 the bruteforce method).

Example 1:
Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
Output: You guessed the secret word correctly.
Explanation:
master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess, and one of them was the secret, so we pass the test case.

Constraints:
1 <= words.length <= 100
words[i].length == 6
words[i] consist of lowercase English letters.
All the strings of wordlist are unique.
secret exists in words.
10 <= allowedGuesses <= 30

Note: Need external implementation in order to test

Tag: G13/50
"""
import collections


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

def find_secret_word(wordlist: list[str], master: 'Masetr') -> None:
    place_counts = collections.defaultdict(int)
    for word in wordlist:
        for i, char in enumerate(word):
            place_counts[str(i)+char] += 1

    def word_uniqueness(word):
        score = 0
        for i, char in enumerate(word):
            score += place_counts[str(i)+char]
        return score

    # wordlist will be sorted from most to least unique.
    wordlist.sort(key=word_uniqueness)

    def word_is_possible(guess_word, word, matches):
        if guess_word == word:
            return False
        match_count = 0
        for a, b in zip(guess_word, word):
            if a == b:
                match_count += 1
        return match_count == matches

    end = -1
    for _ in range(10):
        guess_word = wordlist[end]
        matches = master.guess(guess_word)
        if matches == 6:
            break
        elif matches == 0:
            wordlist = [w for w in wordlist if not any(a==b for a, b in zip(guess_word, w))]
            if end == 0:
                end = -1
        else:
            wordlist = [w for w in wordlist if word_is_possible(guess_word, w, matches)]
            if end == -1:
                end = 0


def main():
    secret = "acckzz"
    words = ["acckzz","ccbazz","eiowzz","abcczz"]
    allowed_guesses = 10
    # Need external implementation access


if __name__ == "__main__":
    main()
