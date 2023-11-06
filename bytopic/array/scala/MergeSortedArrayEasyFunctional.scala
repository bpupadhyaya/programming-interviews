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
// Note: this functional implementation doesn't make use of m and n

object MergeSortedArrayEasyFunctional {
  def main(args: Array[String]): Unit = {
    var nums1 = List(4, 5, 8);
    var nums2 = List(6, 7, 8, 9);
    val m: Int = 3;
    val n: Int = 4;
    var a = merge(nums1, nums2)
    for (num <- a)
      print(s"$num,")
    println();
  }

  def merge(nums1: List[Int], nums2: List[Int]): List[Int] = {
    (nums1, nums2) match {
      case (Nil, Nil) => Nil
      case (x::xs, Nil) => nums1
      case (Nil, y::ys) => nums2
      case (x::xs, y::ys) => {
        if (x <= y)
          x :: merge(nums1.tail, nums2)
        else
          y :: merge(nums1, nums2.tail)
      }
    }
  }
}

// Soln idea / algo:
// 1. Traverse through nums2 and append its elements to the end of nums1 starting from index m.
// 2. Sort the entire nums1 array using library function, sort() in this case.