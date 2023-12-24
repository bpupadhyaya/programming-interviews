"""
Given an integer n, return the number of prime numbers that are strictly less than n.

Example:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Constraints:
0 <= n <= 5 * 10^6

R72/145
"""


def count_primes(n: int) -> int:
    if n < 3:  # No prime number less than 2
        return 0
    lst = [1] * n  # Create a list for marking numbers less than n
    lst[0] = lst[1] = 0  # 0 and 1 are not prime numbers
    m = 2
    while m * m < n:  # we only check a number (m) if its square is less than n
        if lst[m] == 1:  # if m is already marked by 0, no need to check its multiples.
            # If m is marked by 1, we mark all its multiples from m * m to n by 0.
            # 1 + (n - m * m - 1) // m is equal to the number of multiples of m from m * m to n
            lst[m * m: n: m] = [0] * (1 + (n - m * m - 1) // m)
        # If it is the first iteration (e.g. m = 2), add 1 to m (e.g. m = m + 1;
        # which means m will be 3 in the next iteration),
        # otherwise: (m = m + 2); This way we avoid checking even numbers again.
        m += 1 if m == 2 else 2
    return sum(lst)


def main():
    n = 10
    print(count_primes(n))


if __name__ == "__main__":
    main()


"""
Algorithm:
My code is based on the Sieve of Eratosthenes which is efficient yet very simple. Make sure to read the link as well 
as the hints in the description of this question to better understand the Mathmatics of the code. Here, I do not 
want to explain the algorithm, instead I am focused on how to make the code as fast as possible.

Make your code faster:
The code line lst[m * m: n: m] = [0] *((n-m*m-1)//m + 1) is key to reduce the run time. You could write a loop like 
this (but it would be very expensive):
        for i in range(m * m, n,  m):
               lst[i] = 0
After marking all the even indices in the first iteration, I do not check even numbers again, and will only check 
odd numbers in the remaining iterations.
I created a list with numeral elements, instead of boolean elements.
Do not use function sqrt, because it is expensive [do not use: m < sqrt(n)]. Instead, use m * m < n.
"""
