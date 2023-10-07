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
# Soln: Brute Forrce - Merge and Sort

def findMedianOfTwoSortedArrays(data1, data2):
    merged = data1 + data2
    merged.sort()
    merged_length = len(merged)

    if merged_length % 2 ==1:
        return float(merged[merged_length // 2])
    else:
        middle1 = merged[merged_length // 2 -1]
        middle2 = merged[merged_length // 2]
        return (float(middle1) + float(middle2)) / 2.0

def main():
    nums1 = [4,5]
    nums2 = [6,7]
    print('Median of two sorted arrays: ',findMedianOfTwoSortedArrays(nums1, nums2))
    print('\n')

if __name__ == "__main__":
    main()


