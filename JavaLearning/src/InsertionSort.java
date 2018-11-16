public class InsertionSort {
    public static void main(String[] args) {
        int[] myArray = {3, 18, 5, 90, -100, 78, -38, 1003, 2098};
//        int[] myArray = {3, 5, -38, 90, -100, -38, -38, 1003};
//        int[] myArray = {3};
//        int[] myArray = {};

        // To loop over the array N-1 times - N is the number of elements, we start from 1
        for (int unsortedIndex = 1; unsortedIndex < myArray.length; unsortedIndex++) {
            // Save the number ot be inserted in a variable called selectedNumber
            int selectedNumber = myArray[unsortedIndex];

            // Loop over the sorted portion of the array
            for (int sortedIndex = unsortedIndex - 1; sortedIndex >= 0; sortedIndex--) {

                // If the number to be inserted is less than the current sorted number,
                // move the sorted number to right by 1
                if (selectedNumber < myArray[sortedIndex]) {
                    myArray[sortedIndex + 1] = myArray[sortedIndex];
                    // If the current number is at position 0 and the the current number is greater than the number
                    // to be inserted, insert the selected number at position 0
                    if (sortedIndex == 0) {
                        myArray[sortedIndex] = selectedNumber;
                    }
                } else {
                    // If the number to be inserted is greater than or equal to the current sorted number,
                    // insert the number at a higher position
                    myArray[sortedIndex + 1] = selectedNumber;
                    break;
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
}
