//TODO optimize for performance

import java.util.Map;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.LinkedHashMap;
import java.util.Comparator;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.Iterator;

class Name {
    String fName;
    String lName;
    Name(String fName, String lName) {
        this.fName = fName;
        this.lName = lName;
    }
    public String getFName() {
        return this.fName;
    }
    public String getLName() {
        return this.lName;
    }
}

class SortingHashMapCC {
    public static void main(String...args) {
        HashMap<Integer, Name> myMap = new HashMap<Integer,Name>();
        Name n1 = new Name("Tony", "Hoare");
        Name n2 = new Name("James", "Gosling");
        Name n3 = new Name("Ritchie", "Dennis");
        myMap.put(10, n1);
        myMap.put(25, n2);
        myMap.put(1, n3);

        LinkedHashMap<Integer, Name> sortedMap = sortHashMapCC(myMap);

        Set set = sortedMap.entrySet();
        Iterator iterator = set.iterator();
        while (iterator.hasNext()) {
            Map.Entry elm = (Map.Entry) iterator.next();
            System.out.print(elm.getKey() + " -> ");
            System.out.println(myMap.get(elm.getKey()).fName + " " + myMap.get(elm.getKey()).lName);
        }
    }

    private static LinkedHashMap<Integer, Name> sortHashMapCC(HashMap<Integer, Name> myMap) {
        Comparator<Name> compByName = (Name obj1, Name obj2) -> obj1.getFName().compareTo(obj2.getFName());

        LinkedHashMap<Integer, Name> sortedMap = myMap.entrySet().stream()
                .sorted(Map.Entry.<Integer,Name>comparingByValue(compByName))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,(x,y) -> x, LinkedHashMap::new));

        return sortedMap;
    }

}

