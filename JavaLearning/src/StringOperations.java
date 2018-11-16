public class StringOperations {
    public static void main(String[] args) {
        String str1 = new String("This is my first string in Java");
        System.out.println((str1));

        System.out.println(str1.contains("Shounak"));
        System.out.println(str1.equalsIgnoreCase("   This is my first string in Java   ".trim()));
        System.out.println(str1.replace(" ", "_"));

        for (char i : str1.toCharArray()) {
            System.out.println(i);
        }
    }
}
