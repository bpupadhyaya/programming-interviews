// Category: group3
// Given two sorted arrays, return the median of the two sorted arrays.
// The overall run time complexity should be O(log(m+n)), where m is the
// size of first and n is the size of the second array
// Sample: Input: nums1 = [1,4], nums2 = [3]
// Output: 2
// Explanation: merged array = [1,3,4] and the median is 3.
// Sample 2: Input: nums1 = [4,5], nums2 = [6,7]
// Output:
// Explanation: merged array = [4,5,6,7] and the median is (5+6)/2 = 5.5
// Soln: Brute Force - Merge and Sort
package main

import(
    "fmt"
    "sort"
)

func find_median_of_two_sorted_arrays(data1 []int, data2 []int) float32 {
    merged := append(data1, data2...)
    merged_length := len(merged)
    sort.Ints(merged)

    if merged_length % 2 == 1 {
        return (float32)(merged[merged_length / 2])
    } else {
        middle1 := merged[merged_length / 2 - 1]
        middle2 := merged[merged_length / 2]
        return ((float32)(middle1) + (float32)(middle2)) / 2
    }
}

func main() {
    nums1 := []int{4, 5}
    nums2 := []int{6, 7}
    fmt.Printf("Median: %.2f\n", find_median_of_two_sorted_arrays(nums1, nums2))
}