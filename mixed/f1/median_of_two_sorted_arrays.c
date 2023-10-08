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
// Soln: Brute Forrce - Merge and Sort
// TODO: pass pointer to array, instead of copying data, which is expensive for large data set
// Note: use gcc compiler, example: gcc median_of_two_sorted_arrays.c, g++ compiler doesn't recognize qsort(...)

#include <stdio.h>

// Comparison function
int compare (const void * num1, const void * num2) {
   if(*(int*)num1 > *(int*)num2)
    return 1;
   else
    return -1;
}

double findMedianOfTwoSortedArrays(int data1[2], int data2[2]) {
    int merged[4];
    int k = 0;
    for (int i = 0; i < 2; i++) {
        merged[k++] = data1[i];
    }
    for (int i = 0; i < 2; i++) {
        merged[k++] = data2[i];
    }

    //sort merged array
    int merged_length = sizeof(merged) / sizeof(merged[0]);
    qsort(merged, merged_length, sizeof(merged[0]), compare);

    if (merged_length % 2 == 1) {
        return (double)(merged[merged_length / 2]);
    } else {
        int middle1 = merged[merged_length / 2 - 1];
        int middle2 = merged[merged_length / 2];

        return ((double)(middle1) + (double)(middle2)) / 2.0;
    }
}

int main() {
    int nums1[] = {4, 5};
    int nums2[] = {6, 7};
    double median = findMedianOfTwoSortedArrays(nums1, nums2);
    printf("Median: %f\n", median);

}