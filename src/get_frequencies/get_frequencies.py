def get_frequencies(str):
    character_count_dict = {}
    split_string = list(str)
    for item in split_string:
        if item != ' ':
            if item in character_count_dict:
                character_count_dict[item] += 1
            else:
                character_count_dict[item] = 1
    return character_count_dict

	
