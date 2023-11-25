"""
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
There are two types of logs:
- Letter-logs: All words (except the identifier) consist of lowercase English letters.
- Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:
1. The letter-logs come before all digit-logs.
2. The letter-logs are sorted lexicographically by their contents. If their contents are the same,
 then sort them lexicographically by their identifiers.
3. The digit-logs maintain their relative ordering.
Return the final order of the logs.

Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

Example 2:
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

Tag: 937/2927 , R979/2935 , R35/50 (amz)
"""


def reorder_log_files(logs: list[str]) -> list[str]:
    def sort(logs_):
        a, b = logs_.split(' ', 1)
        if b[0].isalpha():
            return 0, b, a
        else:
            return 1, None, None

    return sorted(logs, key=sort)


def reorder_log_files_1(logs: list[str]) -> list[str]:
    def f(x):
        y = x.split(' ', 1)
        return (0, y[1], y[0]) if y[1][0].isalpha() else (1, None, None)

    return sorted(logs, key=f)


def main():
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(reorder_log_files_1(logs))


if __name__ == "__main__":
    main()
