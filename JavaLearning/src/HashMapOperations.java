import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class HashMapOperations {
    public static void main(String[] args) {
        int[] myArray = {1, 3, 2, 3, 4, 2, 3, 4, 5, 4, 5, 4, 5, 1};
        HashMap<Integer, Integer> myHashMap = new HashMap<>();
        for (int i : myArray) {
            if (myHashMap.isEmpty()) {
                myHashMap.put(i, 1);
            } else {
                if (myHashMap.containsKey(i)) {
                    int temp = myHashMap.get(i);
                    myHashMap.replace(i, ++temp);
                } else {
                    myHashMap.put(i, 1);
                }
            }
        }

        Set mySet = myHashMap.entrySet();

        Iterator iter = mySet.iterator();

        while(iter.hasNext()){
            Map.Entry me = (Map.Entry)iter.next();
            System.out.print("Key = " + me.getKey());
            System.out.println(", Value = " + me.getValue());
        }

        System.out.println(myHashMap);
    }
}
