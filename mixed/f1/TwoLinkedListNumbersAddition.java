// Given two non-empty linked lists representing two non-negative integers, stored in reverse order,
// and each of their nodes containing a single digit, find the sum of these two numbers and return
// the result as a linked list.
// Sample:
// Input list1 = [6,5,7], list2 = [9,7,8]
// Output = 756+879 = 1635
// Note: compiles but wrong result, fix the program below.
class ListNode {
    int value;
    ListNode next;

    public ListNode(int value) {
        this.value = value;
    }
    public ListNode(int value, ListNode next) {
        this.value = value;
        this.next = next;
    }
}
class TwoLinkedListNumbersAddition {
    public static void main(String...args){
        ListNode l1 = new ListNode(1);
        l1.next = new ListNode(3);
        l1.next.next = new ListNode(2);

        ListNode l2 = new ListNode(1);
        l2.next = new ListNode(7);
        l2.next.next = new ListNode(5);

        ListNode result = addTwoLinkedListNumbers(l1,l2);
        System.out.print(result.value + "," + result.next.value + "," + result.next.next.value);
        System.out.println();
    }

    static ListNode addTwoLinkedListNumbers(ListNode list1, ListNode list2) {
        ListNode tempListNode = new ListNode(0);
        ListNode current = tempListNode;
        int carry =0;
        while(list1 != null || list2 != null || carry == 1) {
            int sum = 0;
            if(list1 != null) {
                sum += list1.value;
                list1 = list1.next;
            }
            if(list2 != null) {
                sum += list2.value;
                list2 = list2.next;
            }
            sum += carry;
            carry = sum/10;
            ListNode node = new ListNode(sum % 10);
            current.next = node;
            current = current.next;
        }
        return tempListNode.next;
    }
}