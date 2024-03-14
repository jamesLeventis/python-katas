
import math

def get_century(year):
    correct_century_number = math.floor((year / 100) + 1)
    correct_century_string = str(correct_century_number)
    if correct_century_string[-1] == '1':
        suffix = 'st'
    elif correct_century_string[-1] == '2':
        suffix = 'nd'
    elif correct_century_string[-1] == '3':
        suffix = 'rd'
    else:
        suffix = 'th'
    return f'{correct_century_string}{suffix}'
