
def sum_ascii(array):
    ascii_score = 0
    max_name = ""
    for names in array:
        current_score = 0
        for char in names:
            current_score += ord (char)
            if current_score > ascii_score:
                ascii_score = current_score
                max_name = names
    return max_name
    
    
    
    
    
