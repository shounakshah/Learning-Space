public class SelectionSort {
    public static void main(String[] args) {
//        int[] myArray = {3, 5, 18, 90, -100, 78, -38, 1003, 2098};
//        int[] myArray = {3, 5, -38, 90, -100, -38, -38, 1003};
//        int[] myArray = {3};
        int[] myArray = {};

        // To hold the value of the largest element
        int selectedIndex;
        // To loop over the array N-1 times - N is the number of elements
        for (int lastSorted = myArray.length; lastSorted > 1; lastSorted--) {
            selectedIndex = 0;
            for (int i = 1; i < lastSorted; i++) {
                // Sorting the array in ascending order - Logic to select the index of the largest element in the unsorted portion
                if (myArray[i] > myArray[selectedIndex]) {
                    selectedIndex = i;
                }
            }
            swap(myArray, lastSorted - 1, selectedIndex);
        }

        // To account for empty array
        if (myArray.length > 0) {
            System.out.println("Sorted array is: ");
            for (int i = 0; i < myArray.length; i++) {
                System.out.println(myArray[i]);
            }
        } else {
            System.out.println("Empty Array");
        }

    }

    public static void swap(int[] myArray, int i, int j) {
        if (i == j) {
            return;
        }
        int temp = myArray[i];
        myArray[i] = myArray[j];
        myArray[j] = temp;
    }
}
