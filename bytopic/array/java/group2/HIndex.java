// Given an array of integers citations where citations[i] is the number of citations a researcher received for
// their ith paper, return the researcher's h-index.
// According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such
// that the given researcher has published at least h papers that have each been cited at least h times.
// Example:
// Input: citations = [3,0,6,1,5]
// Output: 3
// Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5
// citations respectively.
// Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3
// citations each, their h-index is 3.
//
// Tag: 11/150
// Tag: 274/2927, R710/2936 (overall frequency ranking)

class HIndex {
    public static void main(String[] args) {
        int[] citations = {3,0,6,1,5};
        System.out.println("h-index: " + hIndex(citations));
    }

    static int hIndex(int[] citations) {
        int n = citations.length;
        int[] buckets = new int[n+1];
        for (int c: citations) {
            if (c >= n) {
                buckets[n]++;
            } else {
                buckets[c]++;
            }
        }
        int count = 0;
        for (int i = n; i >= 0; i--) {
            count += buckets[i];
            if (count >= i) {
                return i;
            }
        }
        return 0;
    }
}

// Logic:
// Bucket sort
// assume n is the total number of papers, if we have n+1 buckets, number from 0 to n, then for any paper with
// reference corresponding to the index of the bucket, we increment the count for that bucket. The only exception
// is that for any paper with larger number of reference than n, we put in the n-th bucket.
// Then we iterate from the back to the front of the buckets, whenever the total count exceeds the index of the
// bucket, meaning that we have the index number of papers that have reference greater than or equal to the index.
// Which will be our h-index result. The reason to scan from the end of the array is that we are looking for the
// greatest h-index. For example, given array [3,0,6,5,1], we have 6 buckets to contain how many papers have the
// corresponding index.
// Time complexity ~ O(n)