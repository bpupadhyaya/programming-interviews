"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example:
Input: a = 1, b = 2
Output: 3

Constraints:
-1000 <= a, b <= 1000

R123/145
"""

from math import log, exp


def get_sum(a: int, b: int) -> int:
    # 32 bit mask in hexadecimal
    mask = 0xffffffff
    # works both as while loop and single value check
    while (b & mask) > 0:
        carry = (a & b) << 1
        a = (a ^ b)
        b = carry
    # handles overflow
    return (a & mask) if b > 0 else a


def get_sum_math_1(a: int, b: int) -> int:
    if a == 0 and b != 0:
        return b
    elif b == 0 and a != 0:
        return a
    return int(log(exp(a) * exp(b)))


def get_sum_math_2(a: int, b: int) -> int:
    return int(log(exp(a) * exp(b))) if a != 0 and b != 0 else a or b


def get_sum_math_3(a: int, b: int) -> int:
    return sum([a, b])


def get_sum_math_4(a: int, b: int) -> int:
    while b != 0:
        temp = (a & b) << 1
        a = a ^ b
        b = temp
    return a


def get_sum_math_5(a: int, b: int) -> int:
    ans = [int(i) for i in range(-1000, 1001)]
    return ans[1000 + a + b]


def main():
    a = 3
    b = 2
    print(get_sum_math_5(a, b))


if __name__ == "__main__":
    main()

"""
Explanation of get_sum:
In Python unlike other languages the range of bits for representing a value is not 32, its much much larger than that.
 This is great when dealing with non negative integers, however this becomes a big issue when dealing with negative
  numbers ( two's compliment)

Why ?

Lets have a look, say we are adding -2 and 3, which = 1

In Python this would be ( showing only 3 bits for clarity )

1 1 0 +
0 1 1

Using binary addition you would get

0 0 1

That seems fine but what happended to the extra carry bit ? ( 1 0 0 0 ), if you were doing this by hand you would
 simply ignore it, but Python does not, instead it continues 'adding' that bit and continuing the sum.

1 1 1 1 1 1 0 +
0 0 0 0 0 1 1
0 0 0 1 0 0 0 + ( carry bit )

so this actually continues on forever unless ...

Mask !

The logic behind a mask is really simple, you should know that x & 1 = x right, so using that simple principle,

if we create a series of 4 1's and & them to any larger size series, we will get just that part of the series we
 want, so

1 1 1 1 1 0 0 1
0 0 0 0 1 1 1 1 &

0 0 0 0 1 0 0 1 ( Important to note that using a mask removes the two's compliment)

For this question the platform uses 32 bits, so you just need to create a 32 bit mask of 1's , the quickest way is to
 use hexadecimal and 0xffffffff, you can write the binary form if you prefer it will work the same.

Note the final check, if b = 0 that means the carry bit 'finished', but when there is a negative number ( like -1),
 the carry bit will continue until it exceeds our 32 bit mask ( to end while loop ) it wont be 0 so in that case
  we use the mask.
  
 
get_sum_math_1 explanation:
The main idea is the school formulas for the logarithm:
1. log_base M * N = log_base M + log_base N
2. base^(log_base k) = k

The first gives us the opportunity to get the sum of the logarithms of numbers, and the second to get 
the numbers themselves directly.
math.log(x) method returns the natural logarithm of a number, or the logarithm of number to base math.log(x, base).
Once there were about 15 testcases for this task and there were no problems with zeros. So now I had to add a 
couple of conditions for such cases.

"""