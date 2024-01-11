"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
- BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the
constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
- boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise
  returns false.
- int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the
smallest element in the BST.
You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order
traversal when next() is called.

Sample 1:
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]
Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next()    # return 3
bSTIterator.next()    # return 7
bSTIterator.hasNext() # return True
bSTIterator.next()    # return 9
bSTIterator.hasNext() # return True
bSTIterator.next()    # return 15
bSTIterator.hasNext() # return True
bSTIterator.next()    # return 20
bSTIterator.hasNext() # return False
Note: visualize to understand

Tag: 79/150
Tag: 173/2927, R797/2936 (overall frequency ranking), fb R37/50, M37/50
"""
from typing import Optional, Generator


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.iter = self._inorder(root)
        self.nxt = next(self.iter, None)

    def _inorder(self, node: Optional[TreeNode]) -> Generator[int, None, None]:
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)

    def next(self) -> int:
        res, self.nxt = self.nxt, next(self.iter, None)
        return res

    def has_next(self) -> bool:
        return self.nxt is not None


def main():
    root = TreeNode(7, TreeNode(3), TreeNode(15))
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    bst_iterator = BSTIterator(root)
    print(bst_iterator.next())      # return 3
    print(bst_iterator.next())      # return 7
    print(bst_iterator.has_next())   # return True
    print(bst_iterator.next())      # return 9
    print(bst_iterator.has_next())   # return True
    print(bst_iterator.next())      # return 15
    print(bst_iterator.has_next())   # return True
    print(bst_iterator.next())      # return 20
    print(bst_iterator.has_next())   # return False


if __name__ == "__main__":
    main()
