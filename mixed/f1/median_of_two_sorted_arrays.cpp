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
// Note: Fix the linker error

#include <iostream>
#include <vector>

using namespace std;

double findMedianOfTwoSortedArrays(vector<int>& data1, vector<int>& data2) {
    int m = data1.size();
    int n = data2.size();

    vector<int> merged;
    for (int i = 0; i < m; i++) {
        merged.push_back(data1[i]);
    }
    for (int i = 0; i < n; i++) {
        merged.push_back(data2[i]);
    }

    sort(merged.begin(), merged.end());

    int merged_length = merged.size();

    if (merged_length % 2 == 1) {
        return static_cast<double>(merged[merged_length / 2]);
    } else {
        int middle1 = merged[merged_length / 2 - 1];
        int middle2 = merged[merged_length / 2];


        return (static_cast<double>(middle1) + static_cast<double>(middle2)) / 2.0;
    }
}

int main() {
    vector<int> nums1;
    vector<int> nums2;
    nums1.push_back(4);
    nums1.push_back(5);
    nums2.push_back(6);
    nums2.push_back(7);
    double median = findMedianOfTwoSortedArrays(nums1, nums2);

    cout << median << " ";
}

