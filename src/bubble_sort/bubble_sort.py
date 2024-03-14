def bubble_sort(list):
    if len(list) == 1:
        return list
    swapped = True
    while swapped:
        swapped = False

        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swapped = True
                
    return list
        
	
            
		
            
	
