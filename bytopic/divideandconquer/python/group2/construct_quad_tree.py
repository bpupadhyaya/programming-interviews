"""
Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.
Return the root of the Quad-Tree representing grid.
A Quad-Tree is a tree data structure in which each internal node has exactly four children.
Besides, each node has two attributes:
- val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
 Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
- isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
 class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:
1. If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid
and set the four children to Null and stop.
2. If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid
into four sub-grids. Note: visualize to understand. To learn more about Quad-Tree:
 https://en.wikipedia.org/wiki/Quadtree
3. Recurse for each of the children with the proper sub-grid.

Quad-Tree format:
The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path
terminator where no node exists below.
It is very similar to the serialization of the binary tree. The only difference is that the node is represented
as a list [isLeaf, val].
If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf
or val is False we represent it as 0.

Example:
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the pic representing the Quad-Tree.

Tag: 110/150
Tag: 427/2927, R1755/2936 (overall frequency ranking)
Note: Debug and fix the output
"""


class Node:
    def __init__(self, val=None, is_leaf=None, top_left=None, top_right=None, bottom_left=None, bottom_right=None):
        self.val = val
        self.is_leaf = is_leaf
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right


def construct_fix_this_func(grid: list[list[int]]) -> 'Node':
    def dfs(x=0, y=0, n=len(grid)):
        if all(grid[i+x][j+y] == grid[x][y]
               for i in range(n)
                for j in range(n)):
            return Node(grid[x][y] == 1, True)

        n //= 2

        return Node(False, False,
                    dfs(x, y, n), dfs(x, y+n, n),
                    dfs(x+n, y, n), dfs(x+n, y+n, n))

    return dfs()


def construct(grid: list[list[int]]) -> 'Node':
    def construct_range(top, left, l):
        """
        Construct a node representing the subgrid with
        top left corner at (top, left) and side length l
        """
        if l == 1:
            return Node(grid[top][left], True)
        top_left = construct_range(top, left, l // 2)
        top_right = construct_range(top, left + l // 2, l // 2)
        bot_left = construct_range(top + l // 2, left, l // 2)
        bot_right = construct_range(top + l // 2, left + l // 2, l // 2)

        children = [top_left, top_right, bot_left, bot_right]
        # Check if all sub-grids have the same value
        if all(child.is_leaf and child.val == top_left.val for child in children):
            return Node(top_left.val, True)

        return Node(0, False, top_left, top_right, bot_left, bot_right)

    return construct_range(0, 0, len(grid))


def main():
    grid = [[0, 1], [1, 0]]
    node = construct(grid)
    print("[", node.is_leaf, ",", node.val, "]")
    print("[", node.top_left.is_leaf, ",", node.top_left.val, "]")
    print("[", node.top_right.is_leaf, ",", node.top_right.val, "]")
    print("[", node.bottom_left.is_leaf, ",", node.bottom_left.val, "]")
    print("[", node.bottom_right.is_leaf, ",", node.bottom_right.val, "]")


if __name__ == "__main__":
    main()
