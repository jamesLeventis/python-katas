from src.sum_ascii.sum_ascii import (sum_ascii)

def test_returns_string_when_input_a_list():
    expected = 'a'
    result = sum_ascii(['a'])
    assert type(expected) == type(result)

def test_returns_the_letter_in_ordered_list_with_highest_ASCII_value():
    expected = 'b'
    result = sum_ascii(['a', 'b'])
    assert expected == result

def test_returns_the_letter_in_unordered_longer_list_with_highest_ASCII_value():
    expected = 'd'
    result = sum_ascii(['d', 'b', 'c', 'a'])
    assert expected == result

def test_returns_the_short_word_with_highest_sum_of_ASCII_values_from_short_list():
    expected = 'to'
    result = sum_ascii(['to', 'if'])
    assert expected == result

def test_returns_the_long_word_with_highest_sum_of_ASCII_values_from_long_list():
    expected = 'waterway'
    result = sum_ascii(['sunrise', 'field', 'waterway', 'river', 'lake', 'flower'])
    assert expected == result