class BubbleSort {

    public static void main (String[] args) {
//        int[] myArray = {3, 5, 18, 90, -100, 78, -38, 1003, 2098};
//        int[] myArray = {3, 5, -38, 90, -100, -38, -38, 1003, 2098};
//        int[] myArray = {3};
        int[] myArray = {};

        // Sorting is required ONLY if there are more than 1 elements in the array
        if (myArray.length > 1) {
            for (int lastSorted = myArray.length; lastSorted > 0; lastSorted--) {
                for (int i = 0; i < lastSorted - 1; i++) {

                    // Sorting the array in ascending order
                    if (myArray[i] > myArray[i + 1]) {
                        swap(myArray, i);
                    }
                }
            }
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

    public static void swap(int[] myArray, int i) {
        int temp = myArray[i];
        myArray[i] = myArray[i + 1];
        myArray[i + 1] = temp;
    }
}
