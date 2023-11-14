// Given a reference of a node in a connected undirected graph.
// Return a deep copy (clone) of the graph.
// Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
// class Node {
//     public int val;
//     public List<Node> neighbors;
// }
// Sample 1:
// Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
// Note: visualize to understand
// Output: [[2,4],[1,3],[2,4],[1,3]]
// Explanation: There are 4 nodes in the graph.
// 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
// 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
// 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
// 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
// Note: Check this later and correct the program. clone algo might be correct but graph
// representation needs further work.
//
// Tag: 91/150
// Tag: 133/2927, R936/2936 (overall frequency ranking)

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        this.val = 0;
        this.neighbors = new ArrayList<Node>();
    }
    public Node(int val) {
        this.val = val;
        this.neighbors = new ArrayList<Node>();
    }
    public Node(int val, ArrayList<Node> neighbors) {
        this.val = val;
        this.neighbors = neighbors;
    }
}
class CloneGraph {
    public static void main(String...args){
        ArrayList<Node> neighbors1 = new ArrayList<Node>();
        neighbors1.add(new Node(2));
        neighbors1.add(new Node(4));
        Node node1 = new Node(1, neighbors1);

        ArrayList<Node> neighbors2 = new ArrayList<Node>();
        neighbors2.add(new Node(1));
        neighbors2.add(new Node(3));
        Node node2 = new Node(2, neighbors2);

        ArrayList<Node> neighbors3 = new ArrayList<Node>();
        neighbors3.add(new Node(2));
        neighbors3.add(new Node(4));
        Node node3 = new Node(3, neighbors3);

        ArrayList<Node> neighbors4 = new ArrayList<Node>();
        neighbors4.add(new Node(1));
        neighbors4.add(new Node(3));
        Node node4 = new Node(4, neighbors4);

        // ?? check this graph representation later
        Node graph = new Node(1, neighbors1);

        Node clonedGraph = cloneGraph(graph);
        System.out.println(clonedGraph);
        System.out.println(clonedGraph.neighbors);
    }

    static Node cloneGraph(Node node) {
        if (node == null)
            return null;
        Node copy = new Node(node.val);
        Node[] visited = new Node[101];
        Arrays.fill(visited, null);
        dfs(node, copy, visited);
        return copy;
    }

    private static void dfs(Node node, Node copy, Node[] visited) {
        visited[copy.val] = copy;
        for (Node n: node.neighbors) {
            if (visited[n.val] == null) {
                Node newNode = new Node(n.val);
                copy.neighbors.add(newNode);
                dfs(n, newNode, visited);
            } else {
                copy.neighbors.add(visited[n.val]);
            }
        }
    }
}