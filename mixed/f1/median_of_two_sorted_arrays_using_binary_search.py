# Category: group3
# Given two sorted arrays, return the median of the two sorted arrays.
# The overall run time complexity should be O(log(m+n)), where m is the
# size of first and n is the size of the second array
# Sample: Input: nums1 = [1,4], nums2 = [3]
# Output: 2
# Explanation: merged array = [1,3,4] and the median is 3.
# Sample 2: Input: nums1 = [4,5], nums2 = [6,7]
# Output:
# Explanation: merged array = [4,5,6,7] and the median is (5+6)/2 = 5.5
# Soln: Binary Search

def find_median_of_two_sorted_arrays_using_binary_search(data1, data2):
    n1 = len(data1)
    n2 = len(data2)

    # Ensure data1 is the smaller array for simplicity
    if n1 > n2:
        return find_median_of_two_sorted_arrays_using_binary_search(data2, data1)

    n = n1 + n2
    left = (n1 + n2 + 1) // 2  # Calculate teh left partition size
    low = 0
    high = n1

    while low <= high:
        mid1 = (low + high) // 2  # Calculate mid index for data1
        mid2 = left - mid1  # Calculate mid index ofr data2

        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')

        # Determine values of l1, l2, r1, and r2
        if mid1 < n1:
            r1 = data1[mid1]
        if mid2 < n2:
            r2 = data2[mid2]
        if mid1 - 1 >= 0:
            l1 = data1[mid1 -1]
        if mid2 - 1 >= 0:
            l2 = data2[mid2 -1]

        if l1 <= r2 and l2 <= r1:
            # The partition is correct, we found the median
            if n % 2 == 1:
                return max(l1, l2)
            else:
                return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            # Move towards the left side of data1
            high = mid1 - 1
        else:
            # Move towards the right side of data1
            low = mid1 + 1
    return 0  # If the execution reaches here, the input arrays were not sorted.
def main():
    nums1 = [4,5]
    nums2 = [6,7]
    print('Median of two sorted arrays: ',find_median_of_two_sorted_arrays_using_binary_search(nums1, nums2))
    print('\n')

if __name__ == "__main__":
    main()