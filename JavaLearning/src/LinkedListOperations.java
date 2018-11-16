import java.util.LinkedList;
import java.util.List;

public class LinkedListOperations {
    public static void main(String[] args) {
        int[] myArray = {1, 3, 2, 3, 4, 2, 3, 4, 5, 4, 5, 4, 5, 1};
        List<Integer> myLinkedList = new LinkedList<>();
        for (int i : myArray) {
            myLinkedList.add(i);
        }

        System.out.println(myLinkedList);

        myLinkedList.remove(Integer.valueOf(3));
        myLinkedList.remove(new Integer(3));

        System.out.println(myLinkedList);

        ((LinkedList<Integer>) myLinkedList).removeLastOccurrence(Integer.valueOf(1));

        System.out.println(myLinkedList);

    }
}
