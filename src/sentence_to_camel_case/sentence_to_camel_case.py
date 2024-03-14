def sentence_to_camel_case(arg1, arg2):
    new_capitalized_array = []
    if arg2 == True:
        split_string = arg1.split(' ')
        for item in split_string:
            new_capitalized_array.append(item[0].upper() + item[1:].lower())
   
        
    else:
        split_string = arg1.split(' ')
        new_capitalized_array.append(split_string[0])
        for item in split_string[1:]:
            new_capitalized_array.append(item[0].upper() + item[1:])
    return ''.join(new_capitalized_array)

       