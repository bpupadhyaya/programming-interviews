"""
You are given an array of variable pairs equations and an array of real numbers values,
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string
that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the
answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero
and that there is no contradiction.
Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for
them.

Example:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Tag: 92/150
Tag: 399/2927, R102/2936 (overall frequency ranking)
"""


def dfs(node: str, dest: str, gr: dict, vis: set, ans: list[float], temp: float) -> None:
    if node in vis:
        return
    vis.add(node)
    if node == dest:
        ans[0] = temp
        return
    for ne, val in gr[node].items():
        dfs(ne, dest, gr, vis, ans, temp * val)


def build_graph(equations: list[list[str]], values: list[float]) -> dict:
    gr = {}
    for i in range(len(equations)):
        dividend, divisor = equations[i]
        value = values[i]
        if dividend not in gr:
            gr[dividend] = {}
        if divisor not in gr:
            gr[divisor] = {}
        gr[dividend][divisor] = value
        gr[divisor][dividend] = 1.0 / value

    return gr


def calc_equation(equations: list[list[str]], values: list[float], queries: [list[list[str]]]) -> list[float]:
    gr = build_graph(equations, values)
    final_ans = []

    for query in queries:
        dividend, divisor = query
        if dividend not in gr or divisor not in gr:
            final_ans.append(-1.0)
        else:
            vis = set()
            ans = [-1.0]
            temp = 1.0
            dfs(dividend, divisor, gr, vis, ans, temp)
            final_ans.append(ans[0])
    return final_ans


def main():
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(calc_equation(equations, values, queries))


if __name__ == "__main__":
    main()
