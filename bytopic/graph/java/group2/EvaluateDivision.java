// You are given an array of variable pairs equations and an array of real numbers values,
// where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string
// that represents a single variable.
// You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the
// answer for Cj / Dj = ?.
// Return the answers to all queries. If a single answer cannot be determined, return -1.0.
// Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero
// and that there is no contradiction.
// Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
// Example:
// Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
// queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
// Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
// Explanation:
// Given: a / b = 2.0, b / c = 3.0
// queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
// return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
// note: x is undefined => -1.0
//
// Tag: 92/150
// Tag: 399/2927, R102/2936 (overall frequency ranking)

import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.HashSet;
import java.util.List;
class DivisionEvaluation {
    public static void main(String...args) {
        String[][] equations = {{"a","b"},{"b","c"}};
        double[] values = {2.0, 3.0};
        String[][] queries = {{"a","c"},{"b","a"},{"a","e"},{"a","a"},{"x","x"}};
        List<List<String>> eqnList = new ArrayList<>();
        for (String[] eqn: equations) {
            eqnList.add(Arrays.asList(eqn));
        }
        List<List<String>> queriesList = new ArrayList<>();
        for (String[] query: queries) {
            queriesList.add(Arrays.asList(query));
        }

        double[] result = calcEquation(eqnList, values, queriesList);
        System.out.println("Evaluation result: " + Arrays.toString(result));
    }

    static double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        HashMap<String, HashMap<String, Double>> graph = buildGraph(equations, values);
        double[] finalAns = new double[queries.size()];

        for (int i = 0; i < queries.size(); i++) {
            String dividend = queries.get(i).get(0);
            String divisor = queries.get(i).get(1);

            if (!graph.containsKey(dividend) || !graph.containsKey(divisor)) {
                finalAns[i] = -1.0;
            } else {
                HashSet<String> visited = new HashSet<>();
                double[] ans = {-1.0};
                double temp = 1.0;
                dfs(dividend, divisor, graph, visited, ans, temp);
                finalAns[i] = ans[0];
            }
        }

        return finalAns;
    }

    private static HashMap<String, HashMap<String, Double>> buildGraph(List<List<String>> equations, double[] values) {
        HashMap<String, HashMap<String, Double>> graph = new HashMap<>();

        for (int i = 0; i < equations.size(); i++) {
            String dividend = equations.get(i).get(0);
            String divisor = equations.get(i).get(1);
            double value = values[i];

            graph.putIfAbsent(dividend, new HashMap<>());
            graph.putIfAbsent(divisor, new HashMap<>());

            graph.get(dividend).put(divisor, value);
            graph.get(divisor).put(dividend, 1.0 / value);
        }

        return graph;
    }

    private static void dfs(String node, String dest, HashMap<String, HashMap<String, Double>> graph,
                     HashSet<String> visited, double[] ans, double temp) {
        if (visited.contains(node))
            return;
        visited.add(node);
        if (node.equals(dest)) {
            ans[0] = temp;
            return;
        }

        for (Map.Entry<String, Double> entry: graph.get(node).entrySet()) {
            String ne = entry.getKey();
            double val = entry.getValue();
            dfs(ne, dest, graph, visited, ans, temp * val);
        }
    }
}