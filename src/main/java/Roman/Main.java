package Roman;


public class Main {

    public static void main(String[] args) {

        RomanCalculator Calculator = new RomanCalculator();
        System.out.println(Calculator.add("X","I"));
        System.out.println(Calculator.divide("X","II"));
        System.out.println(Calculator.multiply("X","II"));
        System.out.println(Calculator.subtract("X","II"));
    }
}