from src.roman_numeral_encoder.roman_numeral_encoder import roman_numeral_encoder
def test_returns_an_roman_numeral_from_simple_number():
    input = 1
    expected = 'I'
    result = roman_numeral_encoder(input)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_more_complex_roman_numeral():
    input = 999
    expected = 'CMXCIX'
    result = roman_numeral_encoder(input)
    print(f'Result is: {result}')
    assert result == expected