public class MergeSort {
    public static void main(String[] args) {
//        int[] myArray = {5, 0, -5};
        int[] myArray = {3, 18, 5, 90, -100, 78, -38, 1003, 2098};
//        int[] myArray = {3, 5, -38, 90, -100, -38, -38, 1003};
//        int[] myArray = {3};
//        int[] myArray = {};

        if (myArray.length == 0) {
            System.out.println("Empty Array");
        } else {
            int[] sortedArray = sortArray(myArray);

            System.out.println("Sorted array is: ");
            for (int i = 0; i < sortedArray.length; i++) {
                System.out.println(sortedArray[i]);
            }
        }
    }

    public static int[] sortArray(int[] myArray) {
        if (myArray.length == 1) {
            // If the array has ONLY 1 element return the element as 1 element is always sorted
            return myArray;
        }

        int midIndex = myArray.length / 2;
        int[] leftArray = splitLeftArray(
                myArray,
                0,
                midIndex
        );
        int[] rightArray = splitRightArray(
                myArray,
                midIndex,
                myArray.length
        );

        return sort(
                leftArray,
                rightArray
        );
    }

    public static int[] splitLeftArray(int[] myArray, int startI, int endE) {
        // Base condition to break recursion
        // If the array has ONLY 1 element return the element as 1 element is always sorted
        if (endE - startI == 1) {
            int[] returnArray = new int[1];
            returnArray[0] = myArray[startI];
            return returnArray;
        }

        // If there are more than 1 elements in the array, split it further
        // And sort the returned array
        int midIndex = (startI + endE) / 2;
        return sort(
                splitLeftArray(
                        myArray,
                        startI,
                        midIndex
                ),
                splitRightArray(
                        myArray,
                        midIndex,
                        endE
                )
        );
    }

    public static int[] splitRightArray(int[] myArray, int startI, int endE) {
        // Base condition to break recursion
        // If the array has ONLY 1 element return the element as 1 element is always sorted
        if (endE - startI == 1) {
            int[] returnArray = new int[1];
            returnArray[0] = myArray[startI];
            return returnArray;
        }

        // If there are more than 1 elements in the array, split it further
        // And sort the returned array
        int midIndex = (startI + endE) / 2;
        return sort(
                splitLeftArray(
                        myArray,
                        startI,
                        midIndex
                ),
                splitRightArray(
                        myArray,
                        midIndex,
                        endE
                )
        );
    }

    public static int[] sort(int[] leftArray, int[] rightArray) {
        // This array will hold the sorted elements from both left and right arrays
        int[] sortedArray = new int[leftArray.length + rightArray.length];

        // i will point to left array
        // j will point to right array
        // index will hold the index of sortedArray
        int i = 0, j = 0, index = 0;

        // Loop to create a sorted array
        while (i < leftArray.length || j < rightArray.length) {
            if (i == leftArray.length) {
                // To account for condition where we have gone through all elements of leftArray
                sortedArray[index] = rightArray[j];
                j++;
                index++;
            } else if (j == rightArray.length) {
                // To account for condition where we have gone through all elements of rightArray
                sortedArray[index] = leftArray[i];
                i++;
                index++;
            } else if (leftArray[i] < rightArray[j]) {
                // If array from leftArray is small than element from rightArray, add it to the sortedArray
                sortedArray[index] = leftArray[i];
                i++;
                index++;
            } else {
                // If array from rightArray is small than element from leftArray, add it to the sortedArray
                sortedArray[index] = rightArray[j];
                j++;
                index++;
            }
        }

        return sortedArray;
    }
}
