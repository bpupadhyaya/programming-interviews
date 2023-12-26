"""
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements
to the right of nums[i].

Example:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

R104/145
"""
from bisect import bisect_left


def count_smaller_using_merge_sort(nums: list[int]) -> list[int]:
    res = [0] * len(nums)  # 1
    enum = list(enumerate(nums))  # 2

    merge_sort(enum, 0, len(nums) - 1, res)
    return res


def merge_sort(enum, start, end, res):
    if start >= end:
        return

    mid = start + (end - start) // 2
    merge_sort(enum, start, mid, res)
    merge_sort(enum, mid + 1, end, res)
    merge(enum, start, mid, end, res)


def merge(enum, start, mid, end, res):
    p, q = start, mid + 1
    inversion_count = 0  # 3

    while p <= mid and q <= end:
        if enum[p][1] <= enum[q][1]:
            res[enum[p][0]] += inversion_count  # 5
            p += 1
        else:
            inversion_count += 1  # 4
            q += 1

    while p <= mid:
        res[enum[p][0]] += end - mid
        p += 1

    enum[start:end+1] = sorted(enum[start:end+1], key=lambda e:e[1])


def count_smaller(nums: list[int]) -> list[int]:
    arr, ans = sorted(nums), []  # <-- 1
    for num in nums:
        i = bisect_left(arr, num)  # <-- 2a
        ans.append(i)  # <-- 2b
        del arr[i]  # <-- 2c
    return ans  # <-- 3


def count_smaller_1(nums: list[int]) -> list[int]:
    if len(nums) < 1:
        return []
    arr = []
    res = []
    for num in nums[::-1]:
        index = bisect_left(arr, num)
        res.append(index)
        arr.insert(index, num)
    return res[::-1]


def main():
    nums = [5, 2, 6, 1]
    print(count_smaller_using_merge_sort(nums))


if __name__ == "__main__":
    main()

"""
Explanation for count_smaller:
#   1) Make arr, a sorted copy of the list nums.
#   2) iterate through nums. For each element num in nums:
#       2a) use a binary search to determine the count of elements
#         in the arr that are less than num.
#       2b) append that count to the answer list
#       2c) delete num from arr
#   3) return the ans list 
#   
#   For example, suppose nums = [5,2,6,1] Then arr = [1,2,5,6].
#       num = 5 => binsearch: arr = [1,2,/\5,6], i = 2 => ans = [2,_,_,_], del 5
#       num = 2 => binsearch: arr = [1,/\2,6],   i = 1 => ans = [2,1,_,_], del 2
#       num = 6 => binsearch: arr = [1,/\6],     i = 1 => ans = [2,1,1,_], del 6
#       num = 1 => binsearch: arr = [/\1],       i = 0 => ans = [2,1,1,0], del 1


count_smaller_1 explanation:
The basic logic is to use the bisection algorithm. Traverse the input array in reverse order and try to insert 
each number in a sorted array. The index you get from the bisect.bisect_left() is the left most possible index to 
insert the number, indicating the count of numbers that are smaller than the current number.

count_smaller_using_merge_sort explanation:

NOTE 1: we initialize a list which has the same size as our input array to store the result.

NOTE 2: we initialize another list of tuple to have each tuple stores the index and value as (index, nums[index]). 
This list serves as the bridge to link the array element which is under the sorting process to the result list
 initialized in NOTE 1.

NOTE 3: we create a variable to count the how many numbers from the right half is smaller than the current number
 from the left half.

NOTE 4: when we find that nums[left_index] > nums[right_index], we add 1 to the inversion_count, but we dont add 
the current inversion_count to the final result yet. Because it is still possible that the next number(s) in the 
right half is still smaller than this current left number.

NOTE 5: when we first find a number from the right half that is bigger than the current left number, we know that
 there will not be any number from the right half to be smaller than this current left number. Thus we add this
  inversion_count to the final result through the bridge of enum list.
"""
