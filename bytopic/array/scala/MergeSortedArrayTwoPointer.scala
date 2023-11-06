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
// Soln: two pointer
// Time complexity ~ O(m+n)
// Space complexity ~ O(1)

import scala.util.Sorting;
object MergeSortedArrayTwoPointer {
  def main(args: Array[String]): Unit = {
    var nums1 = Array(4, 5, 8, 0, 0, 0, 0);
    var nums2 = Array(6, 7, 8, 9);
    val m: Int = 3;
    val n: Int = 4;
    merge(nums1, m, nums2, n)
    for (num <- nums1)
      print(s"$num,")
    println();
  }

  def merge(nums1: Array[Int], m: Int, nums2: Array[Int], n: Int): Unit = {
    var i: Int = m - 1
    var j: Int = n - 1
    var k: Int = m + n - 1
    while (j >= 0) {
      if (i >= 0 && nums1(i) > nums2(j)) {
        nums1(k) = nums1(i)
        k -= 1
        i -= 1
      } else {
        nums1(k) = nums2(j)
        k -= 1
        j -= 1
      }
    }
  }
}

// Solution idea:
// The main idea behind multiple pointers is that we start from the highest elements in both the array.
// Compare the highest elements in both the arrays; whichever is higher, copy that to the max. available index
// in nums1. Next, compare two highest available elements again and copy the greater one to the next max. available index
// in nums1. Repeat this process. Our lower bound is index of both nums1 and nums2 should not be less than 0.
// Less than 0 index is not available and that will resutl an error. That is the check we have in the above code:
// while and if LOCs.