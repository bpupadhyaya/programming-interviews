"""
Reverse bits of a given 32 bits unsigned integer.
- Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output
will be given as a signed integer type. They should not affect your implementation, as the integer's internal
binary representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement notation
(https://en.wikipedia.org/wiki/Two%27s_complement). Therefore, in Example 2 above,
the input represents the signed integer -3 and the output represents the signed integer -1073741825.

Example:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
so return 964176192 which its binary representation is 00111001011110000010100101000000.

Tag: 126/150
Tag: 190/2927, R961/2936 (overall frequency ranking)
"""


def reverse_bits(n: int) -> int:
    return int((('{0:032b}'.format(n))[::-1]), 2)


def reverse_bits_using_bit_manipulation(n: int) -> int:
    res = 0
    for _ in range(32):
        res = (res << 1) + (n & 1)
        n >>= 1
    return res


def main():
    n = 43261596
    print(reverse_bits_using_bit_manipulation(n))


if __name__ == "__main__":
    main()
