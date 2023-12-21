"""
You are given an array of integers nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Constraints:
1 <= nums.length <= 10^5
-104 <= nums[i] <= 10^4
1 <= k <= nums.length

Tag: R29/145
"""
import collections


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    d = collections.deque()
    out = []
    for i, n in enumerate(nums):
        print("i = {}, curr element = {}, d = {} and out = {}".format(i, n, d, out))
        while d and nums[d[-1]] < n:
            d.pop()
            print("\t Popped from d because d has elements and nums[d.top] < curr element")
        d.append(i)
        print("\t Added i to d")
        if d[0] == i - k:
            d.popleft()
            print("\t Popped left from d because it's outside the window's leftmost (i-k)")
        if i >= k-1:
            out.append(nums[d[0]])
            print("\t Append nums[d[0]] = {} to out".format(nums[d[0]]))
    return out


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(max_sliding_window(nums, k))


if __name__ == "__main__":
    main()


"""
We maintain a deque of the indexes of the largest elements we've seen (aka "good candidates")
The problem is that we need to maintain sanity of this deque. To this we need to make sure about two things:
Deque should NEVER point to elements smaller than current element
Deque should NEVER point to elements outside our sliding window (which can happen, for instance in above 
example, where the first element is actually the largest element in the whole array, and sort of "clings" to 
the deque, only until we reach an index outside the window it can stretch to, where it's fate has come and it 
shall be removed from the throne!)
We also keep furnishing the deque with curr_element
Finally, and most importantly, we keep appending the front of the deque to our output out.

Complexity:
O(n)
"""
