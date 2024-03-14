from src.caesar_cipher.caesar_cipher import caesar

def test_shifts_one_letter_up_by_one_given_number ():
    input1 = "d"
    input2 = 1
    expected = 'e'
    result = caesar(input1, input2)
    print(f"Result is: {result}")
    assert expected == result

def test_shifts_two_letters_up_by_one_given_number ():
    input1 = "dd"
    input2 = 1
    expected = 'ee'
    result = caesar(input1, input2)
    print(f"Result is: {result}")
    assert expected == result

def test_shifts_two_separate_words_up_by_one_given_number_for_each_letter ():
    input1 = "hello world"
    input2 = 1
    expected = 'ifmmp xpsme'
    result = caesar(input1, input2)
    print(f"Result is: {result}")
    assert expected == result

def test_shifts_more_separate_words_with_non_alphabeticals ():
    input1 = "hello world!"
    input2 = -3
    expected = 'ebiil tloia!'
    result = caesar(input1, input2)
    print(f"Result is: {result}")
    assert expected == result