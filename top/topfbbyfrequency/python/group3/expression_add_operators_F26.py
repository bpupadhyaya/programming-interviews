"""
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary
operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Example:
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Tag: fb R26/50, 282/2927, R550/2936
"""


def add_operators(num: str, target: int) -> list[str]:
    l = len(num)
    ans = set()

    def backtrack(i, total, last, expr):
        if i == l:
            if total == target:
                ans.add(expr)
            return

        for j in range(i, l):
            n = int(num[i:j+1])
            if i == 0:
                backtrack(j+1, n, n, str(n))
            else:
                backtrack(j+1, total+n, n, expr+'+'+str(n))
                backtrack(j+1, total-n, -n, expr+'-'+str(n))
                backtrack(j+1, total-last+last*n, last*n, expr + '*' + str(n))
            if n == 0:
                break

    backtrack(0, 0, 0, '')
    return list(ans)


def main():
    num = "123"
    target = 6
    print("Result: ", add_operators(num, target))


if __name__ == "__main__":
    main()

