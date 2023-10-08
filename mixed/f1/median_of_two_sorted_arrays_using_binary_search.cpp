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
// Soln: Binary Search
// Note: use g++ compiler or equivalent, example: g++ median_of_two_sorted_arrays_using_binary_search.cpp
// gcc compiler produces linker error, it is for C programs

#include <iostream>
#include <vector>

using namespace std;

double find_median_of_two_sorted_arrays_using_binary_search(vector<int>& data1, vector<int>& data2) {
    int n1 = data1.size();
    int n2 = data2.size();

    // Ensure data1 is the smaller array for simplicity
    if (n1 > n2)
        return find_median_of_two_sorted_arrays_using_binary_search(data2, data1);

    int n = n1 + n2;
    int left = (n1 + n2 + 1) / 2; // Calculate te left partition size
    int low = 0, high = n1;

    while (low <= high) {
        int mid1 = (low + high) >> 1; //  Calculate mid index for data1
        int mid2 = left - mid1; // Calculate mid index ofr data2

        int l1 = INT_MIN;
        int l2 = INT_MIN;
        int r1 = INT_MAX;
        int r2 = INT_MAX;

        // Determine values of l1, l2, r1, and r2
        if (mid1 < n1)
            r1 = data1[mid1];
        if (mid2 < n2)
            r2 = data2[mid2];
        if (mid1 - 1 >= 0)
            l1 = data1[mid1 - 1];
        if (mid2 -1 >= 0)
            l2 = data2[mid2 - 1];

        if (l1 <= r2 && l2 <= r1) {
            // The partition is correct, we found the median
            if (n % 2 == 1)
                return max(l1, l2);
            else
                return ((double) (max(l1, l2) + min(r1, r2))) / 2.0;
        } else if (l1 > l2) {
            // Move towards the left side of data1
            high = mid1 - 1;
        } else {
            // Move towards the right of the data1
            low = mid1 + 1;
        }
    }

    return 0; // If the execution reaches here, the input arrays were not sorted.
}

int main() {
    vector<int> nums1;
    vector<int> nums2;
    nums1.push_back(4);
    nums1.push_back(5);
    nums2.push_back(6);
    nums2.push_back(7);
    double median = find_median_of_two_sorted_arrays_using_binary_search(nums1, nums2);

    cout << median << " \n";
}

