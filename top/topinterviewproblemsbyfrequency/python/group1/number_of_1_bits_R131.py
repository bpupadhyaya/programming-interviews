"""
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it
has (also known as the Hamming weight).
Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given
as a signed integer type. It should not affect your implementation, as the integer's internal binary representation
is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input
represents the signed integer. -3.

Example:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Tag: R131/145
Tag: 127/150
Tag: 191/2927, R883/2936 (overall frequency ranking)
"""


def hamming_weight_using_brian_kernighan_algo(n: int) -> int:
    count = 0
    while n != 0:
        n &= n - 1
        count += 1
    return count


def hamming_weight_using_bit_manipulation(n: int) -> int:
    count = 0
    while n != 0:
        count += n & 1
        n >>= 1
    return count


def hamming_weight_using_string_conversion(n: int) -> int:
    binary_string = bin(n)[2:]
    count = binary_string.count('1')
    return count


def main():
    n = 11
    print(hamming_weight_using_string_conversion(n))


if __name__ == "__main__":
    main()
