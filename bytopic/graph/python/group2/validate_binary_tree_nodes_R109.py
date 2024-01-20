"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i],
 return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

Example:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Constraints:
n == leftChild.length == rightChild.length
1 <= n <= 104
-1 <= leftChild[i], rightChild[i] <= n - 1

Tag: R109/2935, 1361/2929
"""
from queue import Queue


def validate_binary_tree_nodes_bfs(n: int, left_child: list[int], right_child: list[int]) -> bool:
    def is_binary_tree_valid(root: int, left_child: list[int], right_child: list[int]) -> bool:
        visited = [False] * len(left_child)  # Tracks visited nodes
        node_queue = Queue()  # Queue for BFS traversal
        node_queue.put(root)
        visited[root] = True

        while not node_queue.empty():
            current = node_queue.get()

            # Check left child
            if left_child[current] != -1:
                if visited[left_child[current]]:  # Check for cycle
                    return False

                node_queue.put(left_child[current])
                visited[left_child[current]] = True  # Mark left child as visited

            # Check right child
            if right_child[current] != -1:
                if visited[right_child[current]]:  # Check for cycle
                    return False

                node_queue.put(right_child[current])
                visited[right_child[current]] = True  # Mark right child as visited

        # Check if there are multiple components
        for visit in visited:
            if not visit:
                return False

        return True  # All nodes form a valid binary tree

    child_count = [False] * n  # Tracks child count for each node

    # Update child count based on leftChild
    for child in left_child:
        # Check if node has child
        if child != -1:
            child_count[child] = True  # Mark left child as having a parent

    # Update child count based on rightChild
    for child in right_child:
        # Check if node has child
        if child != -1:
            if child_count[child]:  # Check if the right child already has a parent
                return False

            child_count[child] = True  # Mark right child as having a parent

    root = -1  # Root node
    for i in range(n):
        if not child_count[i]:
            if root == -1:
                root = i  # Set root node if not assigned
            else:
                return False  # Multiple roots found, not a valid binary tree

    if root == -1:
        return False  # No root found, not a valid binary tree

    return is_binary_tree_valid(root, left_child, right_child)  # Check if the tree is valid


def validate_binary_tree_nodes_dfs(n: int, left_child: list[int], right_child: list[int]) -> bool:
    def is_binary_tree_valid(current: int, left_child: list[int], right_child: list[int], visited: list[int]) -> bool:
        # Check left child
        if left_child[current] != -1:
            if visited[left_child[current]]:  # Check for cycle
                return False

            visited[left_child[current]] = True  # Mark left child as visited
            if not is_binary_tree_valid(left_child[current], left_child, right_child, visited):
                return False

        # Check right child
        if right_child[current] != -1:
            if visited[right_child[current]]:  # Check for cycle
                return False

            visited[right_child[current]] = True  # Mark right child as visited
            if not is_binary_tree_valid(right_child[current], left_child, right_child, visited):
                return False

        return True

    child_count = [False] * n  # Tracks child count for each node

    # Update child count based on leftChild
    for child in left_child:
        # Check if node has child
        if child != -1:
            child_count[child] = True  # Mark left child as having a parent

    # Update child count based on rightChild
    for child in right_child:
        # Check if node has child
        if child != -1:
            if child_count[child]:  # Check if the right child already has a parent
                return False

            child_count[child] = True  # Mark right child as having a parent

    root = -1  # Root node
    for i in range(n):
        if not child_count[i]:
            if root == -1:
                root = i  # Set root node if not assigned
            else:
                return False  # Multiple roots found, not a valid binary tree

    if root == -1:
        return False  # No root found, not a valid binary tree

    visited = [False] * n  # Tracks visited nodes
    visited[root] = True
    if not is_binary_tree_valid(root, left_child, right_child, visited):  # Check if the tree is valid
        return False

    # Check if there is multiple components
    for visit in visited:
        if not visit:
            return False

    return True  # All nodes form a valid binary tree


def main():
    n = 4
    left_child = [1, -1, 3, -1]
    right_child = [2, -1, -1, -1]
    print(validate_binary_tree_nodes_dfs(n, left_child, right_child))


if __name__ == "__main__":
    main()


"""
Implementation explanation:
BFS or DFS
1. Create an array called childCount of size n to track child which nodes have parents.
2. Update Child Count:
Iterate through the leftChild array and For each left child:
If the left child exists (not -1), mark it as having a parent by setting childCount[child] to true.
Iterate through the rightChild array and For each right child:
If the right child exists (not -1), mark it as having a parent by setting childCount[child] to true.
If childCount[child] is true. Then there's multiple parents for this child.
3. Determine Root Node:
Initialize a variable root to -1 (indicating no root found yet).
Iterate through the childCount array and For each node:
If the node has no parent (childCount[node] is false):
If root is -1 (no root assigned yet), set root to the current node.
If root is not -1 (root already assigned):
Return false, indicating multiple roots found.
4. After that, If root is still -1 (no root found):
Return false, indicating no root found (not a valid binary tree).
5. Breadth-First Search for Valid Binary Tree (isBinaryTreeValid):
Initialize a visited array to track visited nodes and queue for BFS traversal.
Mark the root node as visited and enqueue it.
While the queue is not empty:
Dequeue a node and mark it as the current node.
Check the left child of the current node:
If it exists and is already visited, return false (cycle detected).
Enqueue the left child and mark it as visited.
Check the right child of the current node:
If it exists and is already visited, return false (cycle detected).
Enqueue the right child and mark it as visited.
After BFS, check if all nodes were visited:
If any node is unvisited, return false, indicating there's multiple components.
Return true, indicating a valid binary tree.
6. Depth-First Search for Valid Binary Tree (isBinaryTreeValid)
It has the same steps like BFS but we will traverse through the tree recursively.

Complexity
Time complexity: O(N)
Since we are Check for parents in leftChild array with cost N then Check for parents in rightChild array with
 cost N then search for root with cost N then doing BFS or DFS and we will traverse at most all nodes with
  cost N then we check for multiple components with cost N.
The total cost is 5 * N which is O(N).
Space complexity: O(N)
Since we are storing if child has parent with cost N and visited array with cost N and the queue at most can
 have N nodes with cost N.
The total cost is 3 * N which is O(N).

"""
