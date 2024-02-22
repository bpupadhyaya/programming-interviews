import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class StringSortingUsingStreamingAndLambda {
    public static void main(String...args) {
        String[] myArray = {"Banana", "Tea", "Apple", "Tomato"};
        List<String> myList = Arrays.asList(myArray);
        myList.stream().sorted(Comparator.comparing(String::length)).forEach(x -> System.out.println(x));
    }
}
