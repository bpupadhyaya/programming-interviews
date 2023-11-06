// You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two
// integers m and n, representing the number of elements in nums1 and nums2 respectively.
// Merge nums1 and nums2 into a single array sorted in non-decreasing order.
// The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
// To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
// be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
// Example 1:
// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
// Output: [1,2,2,3,5,6]
// Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
// The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
// Soln: two pointer
// Time complexity ~ O(m+n)
// Space complexity ~ O(1)


#include <iostream>
#include <vector>

using namespace std;

void merge_two_sorted_arrays_two_pointer(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int i = m - 1;
    int j = n - 1;
    int k = m + n - 1;

    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
}

int main() {
    vector<int> nums1;
    nums1.push_back(4);
    nums1.push_back(5);
    nums1.push_back(8);
    nums1.push_back(0);
    nums1.push_back(0);
    nums1.push_back(0);
    nums1.push_back(0);

    vector<int> nums2;
    nums2.push_back(6);
    nums2.push_back(7);
    nums2.push_back(8);
    nums2.push_back(9);

    int m = 3;
    int n = 4;
    merge_two_sorted_arrays_two_pointer(nums1, m, nums2, n);
    int size = nums1.size();
    for (int i = 0; i < size; i++) {
        cout << nums1[i] << ", ";
    }
    cout << "\n";

    return 0;
}

// Solution idea:
// The main idea behind multiple pointers is that we start from the highest elements in both the array.
// Compare the highest elements in both the arrays; whichever is higher, copy that to the max. available index
// in nums1. Next, compare two highest available elements again and copy the greater one to the next max. available index
// in nums1. Repeat this process. Our lower bound is index of both nums1 and nums2 should not be less than 0.
// Less than 0 index is not available and that will resutl an error. That is the check we have in the above code:
// while and if LOCs.

