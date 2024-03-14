from src.sentence_to_camel_case.sentence_to_camel_case import (
    sentence_to_camel_case)


def test_returns_a_single_word_in_upper_if_true():
    expected = 'This'
    result = sentence_to_camel_case('this', True)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_single_word_in_lower_if_false():
    expected = 'this'
    result = sentence_to_camel_case('this', False)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_two_words_in_upper_if_true():
    expected = 'ThisDog'
    result = sentence_to_camel_case('this dog', True)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_two_words_first_in_lower_second_in_upper_if_false():
    expected = 'thisDog'
    result = sentence_to_camel_case('this dog', False)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_larger_sentence_in_upper_if_true():
    expected = "ThisBiggerStrangeSentence"
    result = sentence_to_camel_case("This Bigger strange Sentence", True)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_larger_ALLCAPS_sentence_in_upper_if_true():
    expected = "WhyAreYouYelling"
    result = sentence_to_camel_case("WHY ARE YOU YELLING", True)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_an_alternate_capitalized_sentence_in_upper_if_true():
    expected = "ThisIsABitOdd"
    result = sentence_to_camel_case("tHiS iS a BiT oDd", True)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_sentence_in_upper_if_true_ignoring_any_numbers():
    expected = "These1Include2Numbers3"
    result = sentence_to_camel_case("these 1 include 2 numbers 3", True)
    print(f'Result is: {result}')
    assert result == expected