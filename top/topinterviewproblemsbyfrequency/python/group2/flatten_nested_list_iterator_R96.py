"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may
also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.

Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next
should be: [1,1,2,1,1].

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next
should be: [1,4,6].

Constraints:
1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-10^6, 10^6].

R96/145
Note: Needs further work for testing since NestedInteger is externally provided service; provide dummy impl to test
"""


class NestedInteger:
    def is_integer(self) -> bool:

    def get_integer(self) -> int:

    def get_list(self) -> list[NestedInteger]:


class NestedIterator:
    def __init__(self, nested_list: list[NestedInteger]):
        self.stack = nested_list[::-1]

    def next(self) -> int:
        return self.stack.pop().get_integer()

    def has_next(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.is_integer():
                return True
            self.stack = self.stack[:-1] + top.get_list()[::-1]
        return False


class NestedIterator1:
    def __init__(self, nested_list: [NestedInteger]):
        def flatten(nested):
            result = []
            for ni in nested:
                if ni.is_integer():
                    result.append(ni.get_integer())
                else:
                    result.extend(flatten(ni.get_list()))
            return result

        self.flattened = flatten(nested_list)
        self.index = 0

    def next(self) -> int:
        self.index += 1
        return self.flattened[self.index - 1]

    def has_next(self) -> bool:
        return self.index < len(self.flattened)


def main():
    # todo


if __name__ == "__main__":
    main()
