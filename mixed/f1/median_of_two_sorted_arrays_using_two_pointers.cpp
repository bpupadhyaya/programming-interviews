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
// Note: use g++ compiler or equivalent, example: g++ median_of_two_sorted_arrays_using_two_pointers.cpp
// gcc compiler produces linker error, it is for C programs

#include <iostream>
#include <vector>

using namespace std;

double find_median_of_two_sorted_arrays_using_two_pointers(vector<int>& data1, vector<int>& data2) {
    int m = data1.size();
    int n = data2.size();
    int i = 0, j = 0, m1 = 0, m2 = 0;

    // Find median
    for (int count =0; count <= (m + n) / 2; count++) {
        m2 = m1;
        if (i != m && j!= n) {
            if (data1[i] > data2[j]) {
                m1 = data2[j++];
            } else {
                m1 = data1[i++];
            }
        } else if (i < n) {
            m1 = data1[i++];
        } else {
            m1 = data2[j++];
        }
    }

    // Check if the sume of m and n is odd
    if ((m + n) % 2 == 1) {
        return static_cast<double>(m1);
    } else {
        double median_prep = static_cast<double>(m1) + static_cast<double>(m2);
        return median_prep / 2.0;
    }
}

int main() {
    vector<int> nums1;
    vector<int> nums2;
    nums1.push_back(4);
    nums1.push_back(5);
    nums2.push_back(6);
    nums2.push_back(7);
    double median = find_median_of_two_sorted_arrays_using_two_pointers(nums1, nums2);

    cout << "Median: " << median << " \n";
}
