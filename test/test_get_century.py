from src.get_century.get_century import (get_century)

def test_returns_century_as_string():
    expected = str
    result = type(get_century(1950))
    print(f'Result is: {result}')
    assert result == expected

def test_returns_correct_century_with_th_suffix():
    expected = '20th'
    result = get_century(1950)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_different_century_with_th_suffix():
    expected = '18th'
    result = get_century(1750)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_different_century_with_rd_suffix():
    expected = '23rd'
    result = get_century(2243)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_different_century_with_st_suffix():
    expected = '21st'
    result = get_century(2024)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_different_century_with_extra_digit():
    expected = '100th'
    result = get_century(9999)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_different_century_with_extra_digit():
    expected = '101st'
    result = get_century(10000)
    print(f'Result is: {result}')
    assert result == expected