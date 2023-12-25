"""
Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 10^4
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

R78/145
"""


def max_product(nums: list[int]) -> int:
    n = len(nums)
    curr_max_prod_sub_arr = nums[0]
    curr_min_prod_sub_arr = nums[0]
    max_prod_ans = nums[0]

    for i in range(1, n):
        temp = curr_max_prod_sub_arr
        curr_max_prod_sub_arr = max(nums[i], max(curr_max_prod_sub_arr * nums[i], curr_min_prod_sub_arr * nums[i]))
        curr_min_prod_sub_arr = min(nums[i], min(temp * nums[i], curr_min_prod_sub_arr * nums[i]))
        max_prod_ans = max(max_prod_ans, curr_max_prod_sub_arr)
    return max_prod_ans


def max_product_1(nums: list[int]) -> int:
    # DP
    out = max(nums)
    c_max = c_min = 1
    for n in nums:
        temp = c_max * n
        c_max = max(c_min*n, c_max*n, n)
        c_min = min(temp, c_min*n, n)
        out = max(out, c_max)
    return out


def main():
    nums = [2, 3, -2, 4]
    print(max_product_1(nums))


if __name__ == "__main__":
    main()
