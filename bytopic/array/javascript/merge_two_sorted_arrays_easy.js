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

function merge_two_sorted_arrays(nums1, m, nums2, n) {
    for (let i = m, j = 0; j < n; i++, j++) {
        nums1[i] = nums2[j];
    }
    nums1.sort((a,b) => a - b);
}

const nums1 = [4,5,8,0,0,0,0];
const nums2 = [6,7,8,9];
const m = 3;
const n = 4;
merge_two_sorted_arrays(nums1, m, nums2, n);
console.log(nums1);

// Output: [4, 5, 6, 7,8, 8, 9]
// Soln idea / algo:
// 1. Traverse through nums2 and append its elements to the end of nums1 starting from index m.
// 2. Sort the entire nums1 array using library function, sort() in this case.

