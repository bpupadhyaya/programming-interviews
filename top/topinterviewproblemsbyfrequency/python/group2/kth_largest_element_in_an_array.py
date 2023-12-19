"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Constraints:
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

Tag: R19/145
"""
import heapq


def find_kth_largest_using_min_heap(nums: list[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    return heap[0]


def find_kth_largest_using_sort_and_select(nums: list[int], k: int) -> int:
    return sorted(nums, reverse=True)[k-1]


def main():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(find_kth_largest_using_sort_and_select(nums, k))


if __name__ == "__main__":
    main()


"""
Method: Min-heap:
The main idea of this solution is to use a min-heap with a maximum size of k. By doing this, we ensure that the 
smallest of the k largest elements is always on the top of the heap.

Key Data Structures:
heap:
This is a min-heap containing the first k elements of nums. As we progress, we will modify this heap to ensure 
it contains the k largest elements.

Step-by-step Breakdown:
Initialization:
Create a heap with the first k elements of nums.
Transform this list into a min-heap.
Iterate through the List:
For each of the remaining elements in nums:
If the element is larger than the smallest element in the heap (i.e., the top of the heap):
Remove the top element from the heap.
Insert the current element into the heap.
Result:
After processing all elements in nums, the top of the heap will contain the kth largest element. Return this element.

Example:
Consider the list nums = [3,2,1,5,6,4] with k = 2.
Here's the evolution of the heap:
Initial State:
heap: [3,2]
After processing index 2 (element = 1):

heap remains unchanged as 1 is not larger than 2.
After processing index 3 (element = 5):

heap: [3,5]
After processing index 4 (element = 6):

heap: [5,6]
After processing index 5 (element = 4):

heap: [5,6]
The final state of the heap shows that the kth largest element is 5.

Complexity
Time Complexity: O(nlogk)
Each of the n elements is processed once. However, heap operations take O(logk) time, 
leading to an overall complexity of O(nlogk).

Space Complexity: O(k)
The solution uses a heap with a maximum of k elements.


Method: Sort and Select:
This approach is quite straightforward: sort the numbers in descending order and pick the kkk-th element.

Key Data Structures:
List/Array: We use Python's built-in list for this approach. The list is sorted in descending order to get 
the kkk-th largest element.
Step-by-step Breakdown:
Initialization:

Use built-in sorted function to sort the list nums in reverse order (i.e., in descending order).
Selection:

Select the kkk-th element from the sorted list (keeping in mind the zero-based indexing of lists).
Result:

The kkk-th element in the sorted list is the kkk-th largest element in the original list.
Complexity:
Time Complexity: O(NlogN)

Sorting a list of N elements requires O(NlogN) time.
Space Complexity: O(1)

The space used is constant since we are only sorting the original list and selecting an element from it 
without utilizing any additional data structures.

"""
