package Roman;

public class RomanCalculator {
    private RomanConverter romanConverter = new RomanConverter();
    private ArabicConverter arabicConverter = new ArabicConverter();

    public String add(String first, String second) throws IllegalArgumentException {
        int result = romanConverter.romanToInt(first) + romanConverter.romanToInt(second);
        return arabicConverter.intToRoman(result);
    }

    public String subtract(String first, String second) throws IllegalArgumentException {
        int result = romanConverter.romanToInt(first) - romanConverter.romanToInt(second);
        return arabicConverter.intToRoman(result);
    }

    public String multiply(String first, String second) throws IllegalArgumentException {
        int result = romanConverter.romanToInt(first) * romanConverter.romanToInt(second);
        return arabicConverter.intToRoman(result);
    }

    public String divide(String first, String second) throws IllegalArgumentException {
        int result = romanConverter.romanToInt(first) / romanConverter.romanToInt(second);
        if (result == 0) {
            throw new IllegalArgumentException("Division by zero is not allowed in Roman numerals");
        }
        return arabicConverter.intToRoman(result);
    }

}
