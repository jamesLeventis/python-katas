from src.get_distinct_letters.get_distinct_letters import (
    get_distinct_letters)

def test_returns_both_letters_joined_together_from_both_passed_arguments():
    expected = 'ab'
    result = get_distinct_letters('a', 'b')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_unique_letters_from_both_simple_passed_arguments():
    expected = 'ab'
    result = get_distinct_letters('aa', 'bb')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_unique_letters_from_both_longer_passed_arguments_in_alphabetical_order():
    expected = 'dehrw'
    result = get_distinct_letters('hello', 'world')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_unique_letters_from_both_longer_passed_arguments_with_some_capitals_in_alphabetical_order():
    expected = 'LOdehlorw'
    result = get_distinct_letters('hello', 'wOrLd')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_unique_letters_from_both_longer_passed_arguments_with_numbers_in_alphabetical_order():
    expected = '03dhlorw'
    result = get_distinct_letters('h3l1o', 'w0r1d')
    print(f'Result is: {result}')
    assert result == expected
