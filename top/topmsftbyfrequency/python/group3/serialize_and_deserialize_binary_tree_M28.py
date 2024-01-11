"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in
the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
 serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be
 serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not
necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-1000 <= Node.val <= 1000

Tag: R100/145, M28/50
Note: Highly useful for data transformation and storage, also easy to understand.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.i = None

    def serialize(self, root: TreeNode) -> str:
        res = []

        def preorder(root):
            if not root:
                res.append('N')
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        data = data.split(',')
        self.i = 0

        def preorder():
            if data[self.i] == 'N':
                self.i += 1
                return None
            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = preorder()
            root.right = preorder()
            return root
        return preorder()


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))
    print(ans.val, ans.left.val, ans.right.val, ans.right.left.val, ans.right.right.val)


if __name__ == "__main__":
    main()
