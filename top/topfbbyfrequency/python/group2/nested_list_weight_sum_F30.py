"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may
also be integers or other lists.
The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1]
 has each integer's value set to its depth.
Return the sum of each integer in nestedList multiplied by its depth.

Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

Constraints:
1 <= nestedList.length <= 50
The values of the integers in the nested list is in the range [-100, 100].
The maximum depth of any integer is less than or equal to 50.

Note: Need implementation of external class in order to test
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedInteger:
    pass


def depth_sum(nested_list: list[NestedInteger]) -> int:
    # use recursion (dfs)
    def dfs(nested_list_, depth):
        summ = 0  # initialization of the summ
        for element in nested_list_:
            # if the element is integer
            if element.isInteger():
                summ += element.getInteger() * depth  # multiply by the depth
            # if the element is List
            else:
                summ += dfs(element.getList(), depth+1)  # increment the depth by 1
        return summ

    return dfs(nested_list, 1)   # start with depth=1


def main():
    nested_list = [[1, 1], 2, [1, 1]]
    print(depth_sum(nested_list))


if __name__ == "__main__":
    main()

