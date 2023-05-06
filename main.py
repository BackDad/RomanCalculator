class RomanCalculator:
    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral

    def to_decimal(self):
        roman_dict = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        result = 0
        previous_value = 0
        for numeral in self.roman_numeral:
            value = roman_dict[numeral]
            if value > previous_value:
                result += value - 2 * previous_value
            else:
                result += value
            previous_value = value
        return result

    def __add__(self, other):
        decimal_sum = self.to_decimal() + other.to_decimal()
        return RomanCalculator.from_decimal(decimal_sum)

    def __sub__(self, other):
        decimal_difference = self.to_decimal() - other.to_decimal()
        if decimal_difference < 0:
            raise ValueError('Roman numerals cannot represent negative numbers')
        return RomanCalculator.from_decimal(decimal_difference)

    def __mul__(self, other):
        decimal_mult = self.to_decimal() * other.to_decimal()
        return RomanCalculator.from_decimal(decimal_mult)

    def __truediv__(self, other):
        decimal_dividing = self.to_decimal() / other.to_decimal()
        return RomanCalculator.from_decimal(decimal_dividing)

    def __str__(self):
        return self.roman_numeral

    @classmethod
    def from_decimal(cls, decimal_number):
        if not 0 < decimal_number < 4000:
            raise ValueError('Roman numerals can only represent numbers between 1 and 3999')
        roman_dict = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        result = ''
        for value, symbol in roman_dict.items():
            while decimal_number >= value:
                result += symbol
                decimal_number -= value
        return cls(result)


if __name__ == '__main__':
    x = RomanCalculator('XII')
    y = RomanCalculator('II')

    print(f"{x} / {y} =", x / y)
    print(f"{x} - {y} =", x - y)
    print(f"{x} + {y} =", x + y)
    print(f"{x} * {y} =", x * y)
