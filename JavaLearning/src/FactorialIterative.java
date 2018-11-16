import java.util.Scanner;

public class FactorialIterative {
    public static void main(String[] args) {
        System.out.println("Enter an integer to find it's factorial: ");
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();

        // Factorial of 0 and 1 is 1 so, we simply print it
        if (number == 0 || number == 1) {
            System.out.println("Factorial of " + number + " is: 1");
        } else {
            // For numbers other than 0 and 1, we need to calculate factorial
            int factorial = 1;

            // Logic to calculate factorial iteratively
            for (int i = number; i > 1; i--) {
                factorial = factorial * i;
            }
            System.out.println("Factorial of " + number + " is: " + factorial);
        }
    }
}
