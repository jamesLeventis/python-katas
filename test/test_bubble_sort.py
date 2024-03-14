from src.bubble_sort.bubble_sort import (bubble_sort)

def test_returns_list_with_one_number():
    expected = [1]
    result = bubble_sort([1])
    assert expected == result

def test_returns_list_with_both_items_swapped():
    expected = [1, 2]
    result = bubble_sort([2, 1])
    assert expected == result

def test_returns_list_with_front_and_last_items_swapped():
    expected = [1, 2, 3]
    result = bubble_sort([3, 2, 1])
    assert expected == result