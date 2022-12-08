// TODO optimize for performance

import java.util.Map;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.LinkedHashMap;
import java.util.Collections;
import java.util.Comparator;
import java.util.ArrayList;

class SortingHashMapSI {
    public static void main(String...args) {
        HashMap<String, Integer> myMap1 = new HashMap<>();
        LinkedHashMap<String, Integer> sortedMap = new LinkedHashMap<>();
        ArrayList<Integer> list = new ArrayList<>();
        myMap1.put("B", 2);
        myMap1.put("E", 5);
        myMap1.put("A", 1);
        myMap1.put("C", 20);

        sortHashMapSI(myMap1, sortedMap, list);

        System.out.println("Sorted map: " +  sortedMap);
    }

    private static void sortHashMapSI(HashMap<String, Integer> myMap1, LinkedHashMap<String, Integer> sortedMap, ArrayList<Integer> list) {
        for(Map.Entry<String, Integer> entry: myMap1.entrySet()) {
            list.add(entry.getValue());
        }

        Collections.sort(list);

        for (int myNum: list) {
            for (Entry<String, Integer> entry: myMap1.entrySet()) {
                if (entry.getValue().equals(myNum)) {
                    sortedMap.put(entry.getKey(), myNum);
                }
            }
        }
    }

}