from src.get_frequencies.get_frequencies import (get_frequencies)

def test_returns_dictionary():
    expected = {'a': 1}
    result = get_frequencies('a')
    print(f'Result is: {result}')
    assert type(expected) == type(result)

def test_returns_dictionary_with_argument_as_key():
    expected = 'a'
    result = get_frequencies('a')
    print(f'Result is: {result}')
    assert expected in result

def test_returns_dictionary_with_argument_as_key_with_count_as_value():
    expected = {'a': 1}
    result = get_frequencies('a')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_dictionary_with_count_for_each_letter_in_word():
    expected =  { 
'h': 1,
'e': 1,
'l': 2,
'o': 1,

}
    result = get_frequencies("hello")
    print(f'Result is: {result}')
    assert result == expected

def test_returns_dictionary_with_count_for_each_letter_in_sentence():
    expected =  { 
'h': 1,
'e': 1,
'l': 3,
'o': 2,
'w': 1,
'r': 1,
'd': 1
}
    result = get_frequencies("hello world")
    print(f'Result is: {result}')
    assert result == expected

 
 