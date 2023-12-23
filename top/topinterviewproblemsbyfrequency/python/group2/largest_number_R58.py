"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 10^9

Tag: R58/145
"""


def largest_number(nums: list[int]) -> str:
    if not any(map(bool, nums)):
        return '0'
    nums = list(map(str, nums))
    if len(nums) < 2:
        return "".join(nums)

    def compare(x, y):
        return (int(nums[x] + nums[y])) > (int(nums[y] + nums[x]))

    for x in range(len(nums) - 1):
        y = x + 1
        while x < len(nums) and y < len(nums):
            if not compare(x, y):
                nums[y], nums[x] = nums[x], nums[y]
            y += 1
    return "".join(nums)



class LargerNumKey(str):
    def __lt__(x, y):
        # Compare x+y with y+x in reverse order to get descending order
        return x+y > y+x


def largest_number_1(nums: list[int]) -> str:
    # Convert the list of numbers to list of strings
    nums = [str(num) for num in nums]

    # Sort the list of strings using our custom sorting function
    nums.sort(key=LargerNumKey)

    # Join the sorted list of strings to form the final result
    largest_num = ''.join(nums)

    # If the largest number is 0, return "0"
    # Otherwise, return the largest number
    return "0" if largest_num[0] == "0" else largest_num


def largest_number_2(nums: list[int]) -> str:
    import functools

    def comparator(s1, s2):
        if int(s1+s2) < int(s2+s1):
            return -1
        if int(s1+s2) > int(s2+s1):
            return 1
        return 0

    nums = [str(num) for num in nums]
    nums = sorted(nums, key=functools.cmp_to_key(comparator), reverse=True)
    ans = '0' if nums[0] == 0 else ''.join(nums)  # if the biggest number after sorting is 0 in first position,
    # then rest all will also be 0's so return 0
    return ans


def main():
    nums = [3, 30, 34, 5, 9]
    print(largest_number_2(nums))


if __name__ == "__main__":
    main()


"""
largest_number_1 approach:
To solve this problem, we need to sort the given list of numbers such that they form the largest possible number. 
To do this, we need to create a custom sorting function that compares two numbers at a time and concatenates them in 
different orders to see which order forms the larger number. Once we have sorted the numbers, we can concatenate them
 to form the final result.

The LargerNumKey class is a subclass of the built-in str class that overrides the less than operator (<) to compare 
two strings in a special way. The lt method is called when we use the less than operator to compare two strings. 
We define the method to compare two strings x and y in the following way:

Concatenate x and y in reverse order: x+y.
Concatenate y and x in reverse order: y+x.
Compare the two concatenated strings in reverse order to get descending order. That is, if x+y is greater than y+x, 
we return True. Otherwise, we return False.
In the largestNumber method, we first convert the list of numbers to a list of strings. We then sort the list of 
strings using our custom sorting function. Finally, we join the sorted list of strings to form the largest number.

Note that if the largest number is 0, we return "0" instead of the actual largest number. This is because "0" is 
the only case where the leading digit is "0".


largest_number_2 explanation:
## RC ##
## APPROACH : CUSTOM SORTING WITH COMPARATOR ##
## MAIN IDEA : It's all about comparison . We define a func that compares two strings a ,b. we consider a 
bigger than b if a+b > b+a . then we sort the numbers and concatenate them .
## a-> 3, b-> 30 => 330 > 303
## Things to note : Your comparator is supposed to return negative/zero/positive, not a boolean. ##

## ALSO : We can use any type of sort, while sorting instead of comparing two numbers directly, we can use 
the current comparator logic to compare and swap elements accordingly.

## Edge case : o/p -> "00" expected:"0"

## TIME COMPLEXITY : O(NlogN) ##
## SPACE COMPLEXITY : O(N) ##
"""