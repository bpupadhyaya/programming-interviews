"""
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
class Node {
    public int val;
    public List<Node> neighbors;
}

Sample 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Note: visualize to understand
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Note: Check this later and correct the program. clone algo might be correct but graph
representation needs further work.

Tag: 91/150
Tag: 133/2927, R936/2936 (overall frequency ranking)
Note: Debug, note the result structure, and  print all the nodes
"""
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return node
    q, clones = deque([node]), {node.val: Node(node.val, [])}
    while q:
        cur = q.popleft()
        cur_clone = clones[cur.val]

        for ngbr in cur.neighbors:
            if ngbr.val not in clones:
                clones[ngbr.val] = Node(ngbr.val, [])
                q.append(ngbr)
            cur_clone.neighbors.append(clones[ngbr.val])
    return clones[node.val]


def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    graph = [Node(1, [node2, node4]), Node(2, [node1, node3]), Node(3, [node2, node4]),
             Node(4, [node1, node3])]

    res = clone_graph(graph[0])
    print([[res.val, [res.neighbors[0].val, res.neighbors[1].val]],
           # TODO print other nodes
           ])


if __name__ == "__main__":
    main()
