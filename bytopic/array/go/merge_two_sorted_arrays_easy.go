// You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
// the number of elements in nums1 and nums2 respectively.
// Merge nums1 and nums2 into a single array sorted in non-decreasing order.
// The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate
// this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
// Example 1:
// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
// Output: [1,2,2,3,5,6]
// Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
// The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
// Soln: append and sort
// Time complexity ~ O((m+n)log(m+n)), due to sort() function
// Space complexity ~ O(1)

package main

import(
    "fmt"
    "sort"
)

func merge_two_sorted_arrays(data1 []int, m int, data2 []int, n int) {
    for j := 0; j < n; j++ {
        data1[m+j] = data2[j]
    }
    sort.Ints(data1)
}

func main() {
    nums1 := []int{4,5,8,0,0,0,0}
    nums2 := []int{6,7,8,9}
    m := 3
    n := 4
    merge_two_sorted_arrays(nums1,m,nums2,n)
    fmt.Printf("",nums1)
    fmt.Println();
}

// Soln idea / algo:
// 1. Traverse through nums2 and append its elements to the end of nums1 starting from index m.
// 2. Sort the entire nums1 array using library function, sort() in this case.
