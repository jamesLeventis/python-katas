
def vowel_shift(s, n):
    vowels = 'aeiou'
    shifted_string = ''
    
    for char in s:
        if char.lower() in vowels:
            index = vowels.index(char.lower())
            new_index = (index + n) % len(vowels)
            shifted_char = vowels[new_index]
            if char.isupper():
                shifted_char = shifted_char.upper()
            shifted_string += shifted_char
        else:
            shifted_string += char
    
    return shifted_string
    


    list_str[1] = 'o'
    list_str[4] = 'e'
    print(''.join(list_str))