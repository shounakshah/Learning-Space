import java.util.Scanner;

public class FactorialRecursive {
    public static void main(String[] args) {
        // Print out program title
        System.out.println("--- Program to calculate factorial by recursive strategy ---");
        System.out.println();

        // Scan input from console
        System.out.println("Enter a positive integer to find it's factorial: ");
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();

        if (number < 0) {
            // Factorial can ONLY be calculated for non-negative numbers
            System.out.println("You have entered an invalid number. Factorial is ONLY valid for non-negative integers.");
        }else if (number == 0) {
            // Factorial of 0 is 1. No need to calculate anything
            System.out.println("Factorial of 0 is: 1");
        } else {
            // Calculate factorial recursively for all other numbers
            System.out.println("Factorial of " + number + " is: " + calculateFactorial(number));
        }
    }

    public static int calculateFactorial(int number) {
        // Base condition to break recursion
        if (number == 1) {
            return 1;
        }

        // Recursive function call to calculate factorial
        return number * calculateFactorial(number - 1);
    }
}
