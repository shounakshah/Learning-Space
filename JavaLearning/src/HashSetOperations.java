import java.util.HashSet;
import java.util.Iterator;

public class HashSetOperations {
    public static void main(String[] args) {
        int[] myArray = {9, 27, -198, 37, -928, 57, 90, 0};
        HashSet <Integer> mySet = new HashSet<>();
        for (int i : myArray) {
            mySet.add(i);
        }

        System.out.println(mySet);

        String str1 = new String ("Test_String");
        HashSet <Character> myStringSet = new HashSet<>();
        for (char i : str1.toCharArray()) {
            myStringSet.add(i);
        }

        Iterator it = myStringSet.iterator();
        while (it.hasNext()) {
            System.out.println(it.next());
        }

        System.out.println(myStringSet.contains('t'));
        myStringSet.remove('t');
        System.out.println(myStringSet.contains('t'));

    }
}
