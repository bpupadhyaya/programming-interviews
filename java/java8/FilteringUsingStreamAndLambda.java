import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class FilteringUsingStreamAndLambda {
    public static void main(String...args) {
        Integer[] myNumsArray = {1,2,3,4,5};
        List<Integer> myNums = Arrays.asList(myNumsArray);
        List<Integer> filteredNums = myNums.stream().filter(x -> x%2 == 0).collect(Collectors.toList());
        System.out.println(filteredNums);

    }
}

