"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums
except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Tag: R65/145
Tag: 13/150
Tag: 238/2927, R173/2936 (overall frequency ranking)
"""


def product_except_self(nums: list[int]) -> list[int]:
    length = len(nums)
    sol = [1] * length
    pre = 1
    post = 1
    for i in range(length):
        sol[i] *= pre
        pre = pre * nums[i]
        sol[length-i-1] *= post
        post = post * nums[length-i-1]
    return sol


def main():
    nums = [1, 2, 3, 4]
    print(product_except_self(nums))


if __name__ == "__main__":
    main()

"""
Explanation:

Approach
We use the fact that prefix_product of arr[i] is arr[0] * arr[1] * .. * arr[i-1] and postfix_product of arr[i] is 
arr[i+1] * arr[i+2] * .. * arr[n-1].

So basically, we have to calculate prefix_product * postfix_product[i] for each element.

Most solutions implementing the concept of Prefix and Postfix would suggest 2 traversals, however, we 
could one-up that and come up with a single for-loop solution.

1. Initialize a Solution Array of same size as input array with value.
2. Store Prefix and Postfix Product so far in variables.
3. Traverse the input array.
4. Before updating the values for each i, multiply current solution array value at i with the value of prefix
 i.e. multiply with prefix product of the previous i-1 elements.
5. Similarly, calculate the postfix product value for n-i-1 where n is length of input array at each iteration.
6. As in Step 4, before calculating the postfix for i'th value , multiply the solution_array[n-i-1] with the 
postfix product value i.e. products of input[i+1] to input[n-1].

Complexity
Time complexity: O(n) Single Pass 
Space complexity: Technically O(1) as we are not supposed to count the output array.
"""
