"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Input: nums = [1,1,1], k = 2
Output: 2

Constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7

Tag: fb R3/50
"""


def subarray_sum1(nums, k):
    result = 0
    prefix_sum = 0
    d = {0: 1}
    for num in nums:
        prefix_sum = prefix_sum + num
        if prefix_sum - k in d:
            result = result + d[prefix_sum - k]
        if prefix_sum not in d:
            d[prefix_sum] = 1
        else:
            d[prefix_sum] = d[prefix_sum] + 1
    return result


def subarray_sum(nums, k):
    map = {0: 1}
    sum = 0
    result = 0

    for n in nums:
        sum += n
        result += map.get(sum - k, 0)
        map[sum] = map.get(sum, 0) + 1

    return result


def main():
    nums = [1, 1, 1]
    k = 2
    print(subarray_sum1(nums, k))


if __name__ == "__main__":
    main()


"""
Implementation note for subarray_sum:
Initialize variables:
n as the length of the input nums array.
prefix array to store prefix sums, where prefix[i] represents the sum of all elements from index 0 to i in nums.
Initialize prefix[0] with the value of nums[0] as the base case.
Calculate the prefix sums:

Loop through nums starting from the second element.
For each element at index i, update prefix[i] by adding nums[i] to the previous prefix sum prefix[i-1].
This step computes the prefix sums and stores them in the prefix array.
Create an unordered map mp to keep track of prefix sums and their frequencies. Also, initialize cnt (count) to 0, 
which will store the total count of subarrays with the sum equal to k.

Loop through 'nums' once more:

At each step, check if prefix[i] is equal to k. If it is, increment cnt by 1. This handles subarrays that start 
from the beginning of nums and have a sum equal to k.
Check if mp contains a key equal to prefix[i] - k:

If mp contains prefix[i] - k, it means that there exists a subarray with a sum of k ending at index i 
(i.e., a subarray whose sum from some previous index to i is k). In this case, increment cnt by the number 
of such subarrays stored in mp[prefix[i] - k].
Update the frequency of the current prefix[i] in the mp map.

Continue this process for all elements in nums.

Finally, return cnt, which represents the total count of subarrays with a sum equal to k.

Complexity
Time complexity:
O(n)
Space complexity:
O(n)
"""
