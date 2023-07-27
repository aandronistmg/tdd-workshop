def number_to_roman_numeral(number: int) -> str:
    singles = {
        None: '',
        0: '',
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
    }

    tens = {
        None: '',
        10: 'X',
        20: 'XX',
        30: 'XXX',
        40: 'XL',
        50: 'L',
        60: 'LX',
        70: 'LXX',
        80: 'LXXX',
        90: 'XC'
    }

    hundreds = {
        None: '',
        100: 'C',
        200: 'CC',
        300: 'CCC',
        400: 'CD',
        500: "D",
        600: 'DC',
        700: 'DCC',
        800: 'DCCC',
        900: 'CM'
    }

    thousands = {
        None: '',
        1000: 'M',
        2000: 'MM',
        3000: 'MMM'
    }

    thousands_digit = int(str(number // 1000).ljust(4, '0'))
    thousands_digit = thousands_digit if thousands_digit != 0 else None

    hundreds_digit = int(str((number % 1000) // 100).ljust(3, '0'))
    hundreds_digit = hundreds_digit if hundreds_digit != 0 else None

    tens_digit = int(str(number % 100 // 10).ljust(2, '0'))
    tens_digit = tens_digit if tens_digit != 0 else None

    units_digit = (number % 10)

    return f"{thousands[thousands_digit]}{hundreds[hundreds_digit]}{tens[tens_digit]}{singles[units_digit]}"
