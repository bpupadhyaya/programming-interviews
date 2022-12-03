// Given an array of words and a width, format the text such that each line has exactly
// given width characters and is fully justified.
// Sample Input and Output:
// Input: words = ["Here", "is", "an", "academy", "of", "best", "psychobiology."], maxWidth = 16
// Output:
// [
//   "Here    is    an",
//   "academy  of best",
//   "psychobiology.  "
//]

import java.util.List;
import java.util.ArrayList;

class TextJustification {
    public static void main(String[] args) {
        int givenWidth = 15;
        String[] words = {"Here", "is", "an", "academy", "of", "best", "psychobiology."};
        // TODO not exactly right, need to debug
        List<String> myLines = justify(words, givenWidth);
        for(String line: myLines) {
            System.out.println(line);
        }
    }

    private static List<String> justify(String[] words, int width) {
        List<String> lines = new ArrayList<String>();
        int index = 0;
        while (index < words.length) {
            int count = words[index].length();
            int last = index +1;
            while (last < words.length) {
                if (words[last].length() + count + 1 > width)
                    break;
                count += words[last].length() + 1;
                last++;
            }

            StringBuilder builder = new StringBuilder();
            int diff = last - index - 1;
            if(last == words.length || diff == 0) {
                for(int i = index; i < last; i++) {
                    builder.append(words[i] + " ");
                }
                builder.deleteCharAt(builder.length() - 1);
                for (int i = builder.length(); i < width; i++) {
                    builder.append(" ");
                }
            } else {
                int spaces = (width - count ) / diff;
                int rt = (width - count) / diff;
                for (int i = index; i < last; i++) {
                    builder.append(words[i]);
                    if (i < last - 1) {
                        for (int j = 0; j <= (spaces + ((i - index) < rt ? 1 : 0 )); j++) {
                            builder.append(" ");
                        }
                    }
                }
            }
            lines.add(builder.toString());
            index = last;
        }
        return lines;
    }

}