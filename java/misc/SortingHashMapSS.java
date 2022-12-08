// TODO optimize for performance
import java.util.Map;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.LinkedHashMap;
import java.util.Collections;
import java.util.Comparator;
import java.util.ArrayList;

class SortingHashMapSS {
    public static void main(String...args) {
        HashMap<String, String> myMap1 = new HashMap<>();
        LinkedHashMap<String, String> sortedMap = new LinkedHashMap<>();
        ArrayList<String> list = new ArrayList<>();
        myMap1.put("5", "E");
        myMap1.put("1", "A");
        myMap1.put("2", "B");

        sortHashMapSS(myMap1, sortedMap, list);

        System.out.println("Sorted map: " +  sortedMap);
    }

    private static void sortHashMapSS(HashMap<String, String> myMap1, LinkedHashMap<String, String> sortedMap, ArrayList<String> list) {
        for(Map.Entry<String, String> entry: myMap1.entrySet()) {
            list.add(entry.getValue());
        }

        Collections.sort(list, new Comparator<String>() {
            public int compare(String str1, String str2) {
                return str1.compareTo(str2);
            }
        });

        for (String myString: list) {
            for (Entry<String, String> entry: myMap1.entrySet()) {
                if (entry.getValue().equals(myString)) {
                    sortedMap.put(entry.getKey(), myString);
                }
            }
        }
    }

}