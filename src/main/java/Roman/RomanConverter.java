package Roman;

public class RomanConverter {

    private static final int[] VALUES = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    private static final String[] SYMBOLS = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    public int romanToInt(String s) {
        int result = 0;
        int i = 0;
        for (int j = 0; j < VALUES.length; j++) {
            while (s.startsWith(SYMBOLS[j], i)) {
                result += VALUES[j];
                i += SYMBOLS[j].length();
            }
        }
        return result;
    }

}
