from src.lengthen_date.lengthen_date import (lengthen_date)

def test_returns_a_string():
    expected = str
    result = type(lengthen_date('21.03.2017'))
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_full_date_as_string():
    expected = 'Tuesday 21st March 2017'
    result = lengthen_date('21.03.2017')
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_full_date_as_string_with_nd_suffix():
    expected = 'Wednesday 22nd March 2017'
    result = lengthen_date('22.03.2017')
    print(f'Result is: {result}')
    assert result == expected
def test_returns_a_full_date_as_string_with_rd_suffix():
    expected = 'Thursday 23rd March 2017'
    result = lengthen_date('23.03.2017')
    print(f'Result is: {result}')
    assert result == expected
def test_returns_a_full_date_as_string_with_th_suffix():
    expected = 'Friday 24th March 2017'
    result = lengthen_date('24.03.2017')
    print(f'Result is: {result}')
    assert result == expected