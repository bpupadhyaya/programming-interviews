"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left
of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves
right by one position.

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


Tag: 239/2927 , R48/2935 , R6/50 (amz)
"""


from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    res = []
    left = right = 0
    q = deque()

    while right < len(nums):
        while q and nums[right] > nums[q[-1]]:
            q.pop()
        q.append(right)

        if left > q[0]:
            q.popleft()

        if right + 1 >= k:
            res.append(nums[q[0]])
            left += 1
        right += 1

    return res


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(max_sliding_window(nums, k))


if __name__ == "__main__":
    main()


"""
Approach
This is based on Python. Other might be different a bit.

1. Initialize Variables:
- Initialize an empty list res to store the result.
- Initialize two pointers left and right to represent the sliding window.
- Initialize an empty deque q to maintain indices of potentially maximum elements.

2. Sliding Window Loop:
- While the right pointer is within the range of nums:
--Compare nums[right] with the elements at the back of the deque q.
---If q is not empty and nums[right] is greater than nums[q[-1]], remove the back element of q since it cannot 
   be the maximum for the current window.
--Append the current right index to the back of the deque q.

3. Adjust Left Pointer:
- If the index at the front of q (maximum element index) is less than the left pointer, remove the front element 
 of q since it's no longer relevant for the current window.

4. Calculate and Store Maximum Element:
-If the current window size is equal to or larger than k:
--Append the maximum element of the current window (the element at index q[0]) to the res list.

5. Adjust Left Pointer and Move Right Pointer:
-Increment the left pointer by 1.

6. Move Right Pointer:
-Increment the right pointer by 1.

7. Return Result:
- Return the res list containing the maximum elements for each sliding window.

Complexity
-Time complexity: O(N)
 N is the length of the input nums list. This is because both the left and right pointers traverse the nums list 
 once, and each element is processed only once when added to or removed from the deque q.

-Space complexity: O(K)
 K is the size of the sliding window. The deque q can store at most K indices representing the maximum elements 
 within the sliding window. The res list also requires O(K) space to store the maximum elements for each window.
"""
