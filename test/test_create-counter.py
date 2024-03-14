from src.create_counter.create_counter import (create_counter)

def test_create_counter_outputs_a_dictionary():
    expected = dict
    counter = create_counter(1)
    result = counter
    assert expected == type(result)

def test_create_counter_increases():
    expected = 2
    counter = create_counter(1)
    up = counter['up']
    result = up()
    print(f'Result is: {result}')
    assert result == expected

def test_create_counter_decreases():
    expected = 0
    counter = create_counter(1)
    down = counter['down']
    result = down()
    print(f'Result is: {result}')
    assert result == expected

def test_create_counter_outputs_the_number_passed_in():
    expected = 1
    counter = create_counter(1)
    up = counter['up']
    down = counter['down']
    up()
    result = down()
    print(f'Result is: {result}')
    assert result == expected


