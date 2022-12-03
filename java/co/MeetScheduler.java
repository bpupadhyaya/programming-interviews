// Find the earliest time slot that works for two people given their availability time slots and meeting duration.
// Sample input and output:
// Input: s1 = [[5,10],[20,50],[70,85]], s2 = [[7, 12],[40,60],[80,90]], duration = 10
// Output: [40,50]

import java.util.PriorityQueue;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class MeetingScheduler {
    public static void main(String... args) {
        int[][] p1Slots = {{5,10},{20,50},{70,85}};
        int[][] p2Slots = {{7,12},{40,60},{80,90}};
        int duration = 10;

        List<Integer> meet = findMeetingDuration(p1Slots, p2Slots, duration);
        for (Integer myTime: meet) {
            System.out.print(myTime+", ");
        }
        System.out.println();
    }

    private static List<Integer> findMeetingDuration(int[][] s1, int[][] s2, int d) {
        PriorityQueue<int[]> slots = new PriorityQueue<>((st1, st2) -> st1[0] - st2[0]);

        for (int[] slot: s1) {
            if (slot[1] - slot[0] >= d)
                slots.offer(slot);
        }

        for(int[] slot: s2) {
            if (slot[1] - slot[0] >= d)
                slots.offer(slot);
        }

        while (slots.size() > 1) {
            int[] slt1 = slots.poll();
            int[] slt2 = slots.peek();
            if (slt1[1] >= slt2[0] + d) {
                return new ArrayList<Integer>(Arrays.asList(slt2[0], slt2[0] + d));
            }
        }

        return new ArrayList<Integer>();
    }
}