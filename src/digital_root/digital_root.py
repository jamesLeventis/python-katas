def digital_root(num):
    number_string = str(num)
    sum_total = 0
    for digit in number_string:
        sum_total += int(digit) 
    if sum_total >= 10:
        return digital_root(sum_total)
    else:
        return sum_total

print(type(4))
    