// You are given a list of airline tickets where tickets[i] = [from_i, to_i] represent the departure and
// the arrival airports of one flight. Reconstruct the itinerary in order and return it.
// All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
// If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical
// order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order
// than ["JFK", "LGB"]. You may assume all tickets form at least one valid itinerary. You must use all the
// tickets once and only once.
// Sample 1:
// Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
// Output: ["JFK","MUC","LHR","SFO","SJC"]

import java.util.Map;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;

class ReconstructItinerary {
    public static void main(String...args) {
        List<List<String>> tickets = List.of(
                List.of("MUC","LHR"),
                List.of("JFK","MUC"),
                List.of("SFO","SJC"),
                List.of("LHR","SFO")
        );

        List<String> itinerary = reconstructItinerary(tickets);
        for (String item: itinerary) {
            System.out.print(item + ", ");
        }
        System.out.println();

    }

    static List<String> reconstructItinerary(List<List<String>> tickets) {
        Map<String, PriorityQueue<String>> graph = new HashMap<>();

        for (List<String> ticket: tickets) {
            graph.putIfAbsent(ticket.get(0), new PriorityQueue<>());
            graph.get(ticket.get(0)).add(ticket.get(1));
        }

        LinkedList<String> itinerary = new LinkedList<>();
        dfs("JFK", graph, itinerary);

        return itinerary;
    }

    private static void dfs(String airport, Map<String, PriorityQueue<String>> graph, LinkedList<String> itinerary) {
        PriorityQueue<String> nextAirports = graph.get(airport);
        while (nextAirports != null && !nextAirports.isEmpty()) {
            dfs(nextAirports.poll(), graph, itinerary);
        }
        itinerary.addFirst(airport);
    }
}

// Soln:
// Time and Space Complexity
// Time Complexity: O(NlogN) due to sorting the tickets.
// Space Complexity: O(N), for storing the graph and the itinerary.
