"""
You are given an integer array arr.
We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating
them, the result should equal the sorted array.
Return the largest number of chunks we can make to sort the array.

Example 1:
Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.

Constraints:
1 <= arr.length <= 2000
0 <= arr[i] <= 10^8

Tag: M35/50
"""


def max_chunks_to_sorted(arr: list[int]) -> int:
    st = []
    for n in arr:
        if len(st) == 0 or st[-1] <= n:
            st.append(n)
        else:
            ma = st[-1]
            while st and st[-1] > n:
                ma = max(ma, st.pop())
            st.append(ma)

    return len(st)


def main():
    arr = [5, 4, 3, 2, 1]
    print(max_chunks_to_sorted(arr))


if __name__ == "__main__":
    main()
