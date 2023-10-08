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
# Soln: Two Pointers

def find_median_of_two_sorted_arrays_using_two_pointers(data1, data2):
    m = len(data1)
    n = len(data2)
    i = 0
    j = 0
    m1 = 0
    m2 = 0

    # Find median
    for count in range(0, (m + n) // 2 + 1):
        m2 = m1
        if i <n and j < m:
            if data1[i] > data2[j]:
                m1 = data2[j]
                j +=1
            else:
                m1 = data1[i]
                i +=1
        elif i < n:
            m1 = data1[i]
            i += 1
        else:
            m1 = data2[j]
            j += 1

    # Check if the sum of m and n is odd
    if (m + n) % 2 == 1:
        return float(m1)
    else:
        median_prep = float(m1) + float(m2)
        return median_prep / 2.0

def main():
    nums1 = [4,5]
    nums2 = [6,7]
    print('Median of two sorted arrays: ',find_median_of_two_sorted_arrays_using_two_pointers(nums1, nums2))

if __name__ == "__main__":
    main()