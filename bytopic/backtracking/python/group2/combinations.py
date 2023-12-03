"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Tag: 102/150
Tag: 77/2927, R335/2936 (overall frequency ranking)
"""


def combine_using_iterative(n: int, k: int) -> list[list[int]]:
    def generate_combinations(elems, num):
        elems_tuple = tuple(elems)
        total = len(elems_tuple)
        if num > total:
            return
        curr_indices = list(range(num))
        while True:
            yield tuple(elems_tuple[i] for i in curr_indices)
            for idx in reversed(range(num)):
                if curr_indices[idx] != idx + total - num:
                    break
            else:
                return
            curr_indices[idx] += 1
            for j in range(idx+1, num):
                curr_indices[j] = curr_indices[j-1] + 1
    return [list(combination) for combination in generate_combinations(range(1, n+1), k)]


def combine_using_backtracking(n: int, k: int) -> list[list[int]]:
    def backtrack(first=1, curr=[]):
        if len(curr) == k:
            output.append(curr[:])
            return
        for i in range(first, n + 1):
            curr.append(i)
            backtrack(i+1, curr)
            curr.pop()
    output = []
    backtrack()
    return output


def main():
    n = 4
    k = 2
    print(combine_using_backtracking(n, k))


if __name__ == "__main__":
    main()
