// A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
// Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation
// is defined as one single character changed in the gene string.
// For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
// There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a
// valid gene string.
// Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations
// needed to mutate from startGene to endGene. If there is no such a mutation, return -1.
// Note that the starting point is assumed to be valid, so it might not be included in the bank.
// Example:
// Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
// Output: 2
//
// Tag: 96/150
// Tag: 433/2927, R1250/2936 (overall frequency ranking)

import java.util.Set;
import java.util.HashSet;
import java.util.Queue;
import java.util.LinkedList;
class MinimumGeneticMutation {
    public static void main(String...args) {
        String startGene = "AACCGGTT";
        String endGene = "AAACGGTA";
        String[] bank = {"AACCGGTA","AACCGCTA","AAACGGTA"};

        System.out.println("Min. mutations: " + minMutation(startGene, endGene, bank));
    }

    static int minMutation(String startGene, String endGene, String[] bank) {
        int level = 0, len = bank.length;
        char[] chars = {'A', 'C','G','T'}; // Used to generate possible mutations

        Set<String> hashSet = new HashSet<String>(); // Used to store all valid mutatoins

        for (String s: bank)
            hashSet.add(s);

        Queue<String> queue = new LinkedList<>(); // To implement BFS
        queue.add(startGene);

        while (true) {
            ++level;
            int n = queue.size();

            if (n == 0) return -1; // No gene string left to generate any other mutation

            for (int i = 0; i < n; i++) {
                char[] ch = queue.poll().toCharArray();

                for (int j = 0; j < 8; j++) { // We check every letter of gene string
                    char orgChar = ch[j];
                    for (int c = 0; c < 4; c++) { // Trying all possible mutation with the given gene string
                        ch[j] = chars[c];
                        String str = String.valueOf(ch);
                        if (str.equals(endGene) && hashSet.contains(str)) // Return if end gene is found and is valid
                            return level;
                        if (hashSet.contains(str) == false)
                            continue;
                        hashSet.remove(str);
                        queue.add(str);
                    }
                    ch[j] = orgChar;
                }
            }
        }
    }
}