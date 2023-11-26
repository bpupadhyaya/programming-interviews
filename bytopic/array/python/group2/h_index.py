"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for
their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such
that the given researcher has published at least h papers that have each been cited at least h times.

Example:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5
citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3
citations each, their h-index is 3.

Tag: 11/150
Tag: 274/2927, R710/2936 (overall frequency ranking)
"""


def h_index(citations: list[int]) -> int:
    citations.sort(reverse=True)
    if len(citations) == 1 and citations[0] > 0:
        return 1
    if citations[-1] >= len(citations):
        return len(citations)
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
    return 0


def main():
    citations = [3, 0, 6, 1, 5]
    print(h_index(citations))


if __name__ == "__main__":
    main()

"""
Approach
The solution begins by sorting the array of citations in reverse order, ensuring that the papers with the highest 
citation counts are at the beginning. Next, several conditions are checked to determine the h-index. First, 
if the array contains only one element and it is greater than zero, the h-index is 1. If the smallest value in 
the sorted array is greater than or equal to the length of the array, the h-index is equal to the array length. 
Otherwise, the array is traversed, and for each index i, the value at that index is compared to i+1. If the value 
is less than i+1, i is returned as the h-index. If none of the conditions are met, the h-index is 0.

Complexity
Time complexity:
The time complexity of the solution primarily depends on the sorting operation, which has a time complexity 
of O(n log n), where n is the length of the input array. The subsequent iterations through the array and the 
condition checks have a linear time complexity of O(n). Therefore, the overall time complexity is O(n log n).

Space complexity:
The solution has a space complexity of O(1) since it only uses a constant amount of extra space to store 
variables and does not depend on the input size. No additional data structures are employed, and the sorting 
operation is performed in-place.
"""