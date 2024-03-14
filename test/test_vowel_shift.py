from src.vowel_shift.vowel_shift import vowel_shift

def test_returns_a_string():
    input = 'foo'
    expected = str
    result = type(vowel_shift(input))
    print(f"Result is: {result}")
    assert expected == result

def test_returns_a_string():
    input1 = 'hello'
    input2 = 1
    expected = 'holle'
    result = vowel_shift(input1, input2)
    print(f"Result is: {result}")
    assert expected == result