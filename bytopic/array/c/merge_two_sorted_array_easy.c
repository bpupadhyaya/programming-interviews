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
// Time complexity ~ O((m+n)log(m+n)), due to sorting function??? (lookup qsort time complexity)
// Space complexity ~ O(1)
// Typical compilation command (Mac OS):
// gcc <source_file_name>
// eg: gcc merge_two_sorted_arrays_easy.cpp
// Typical run command :
// ./<output_filename>
// eg: ./a.out
// Note: sorting is not working, debug and fix it.


#include <stdio.h>

// Comparison function
int compare (const void * num1, const void * num2) {
   if(*(int*)num1 > *(int*)num2)
    return 1;
   else
    return -1;
}

void merge_two_sorted_arrays(int nums1[7], int m, int nums2[4], int n) {
    for (int j = 0, i = m; j < n; j++) {
        nums1[i] = nums2[j];
        i++;
    }

    // Sort merged array
    int nums1_length = sizeof(nums1) / sizeof(nums1[0]);
    qsort(nums1, nums1_length, sizeof(nums1[0]), compare);
}

int main() {
    int nums1[] = {4,5,8,0,0,0,0};
    int nums2[] = {6,7,8,9};
    int m = 3;
    int n = 4;
    merge_two_sorted_arrays(nums1, m, nums2, n);
    int length = sizeof(nums1) / sizeof(nums1[0]);
    for (int i = 0; i < length; i++) {
        printf("%d,", nums1[i]);
    }
    printf("\n");
}

// Soln idea / algo:
// 1. Traverse through nums2 and append its elements to the end of nums1 starting from index m.
// 2. Sort the entire nums1 array using library function, sort() in this case.

