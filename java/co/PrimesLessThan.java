// Given an integer n, return the number of prime numbers that are strictly less than n.
class PrimeLessThan {
    public static void main(String... args) {
        int p = 17;
        int count = 0;
        for (int i = 2; i < p; i++) {
            boolean prime = true;
            for (int j = 2; j <= i-1; j++) {
                if (i % j == 0)
                    prime = false;
            }
            if (prime) {
                count++;
            }
        }

        System.out.println("Count: " + count);

    }
}