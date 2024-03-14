def get_distinct_letters(str1, str2):
	set1 = set(str1)
	set2 = set(str2)
	unique_set1 = set1 - set2
	unique_set2 = set2 - set1

	distinct_letters = sorted(unique_set1.union(unique_set2))
	return ''.join(distinct_letters)
