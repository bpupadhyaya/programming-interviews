import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class FindingSquareUsingStreamAndMap {
    public static void main(String...args) {
        Integer[] myNumsArray = {1,2,3,4,5};
        List<Integer> myNums = Arrays.asList(myNumsArray);
        myNums.stream().map(x -> x * x).forEach(x -> System.out.println(x));

//        List<Integer> squared = myNums.stream().map(x -> x * x).collect(Collectors.toList());
//        System.out.println(squared);

    }
}
