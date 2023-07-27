from src.roman_numerals import number_to_roman_numeral

def test_number_to_roman_numeral_returns_string():
    expected = str
    actual = type(number_to_roman_numeral(number=1))

    assert actual == expected


def test_number_to_roman_numeral_returns_I_if_number_is_1():
    expected = 'I'
    actual = number_to_roman_numeral(number=1)

    assert actual == expected


def test_number_to_roman_numeral_returns_VIII_if_number_is_8():
    expected = 'VIII'
    actual = number_to_roman_numeral(number=8)

    assert actual == expected


def test_number_to_roman_numeral_returns_LX_if_number_is_60():
    expected = 'LX'
    actual = number_to_roman_numeral(number=60)

    assert actual == expected


def test_number_to_roman_numeral_returns_DCLXVI_if_number_is_666():
    expected = 'DCLXVI'
    actual = number_to_roman_numeral(number=666)

    assert actual == expected


def test_number_to_roman_numeral_returns_MMMDCCCXCII_if_number_is_3892():
    expected = 'MMMDCCCXCII'
    actual = number_to_roman_numeral(number=3892)

    assert actual == expected
