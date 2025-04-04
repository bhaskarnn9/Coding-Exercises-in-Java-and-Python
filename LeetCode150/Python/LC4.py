# merge -> find median

def median_of_two_sorted_arrays(list1, list2):
	merged = []

	i, j = 0, 0
	len1, len2 = len(list1), len(list2)

	while i < len1 and j < len2:
		if list1[i] < list2[j]:
			merged.append(list1[i])
			i += 1
		else:
			merged.append(list2[j])
			j += 1

	merged +=  list1[i:] + list2[j:]

	if len(merged)%2 == 0:
		return (merged[len(merged)//2] + merged[len(merged)//2 - 1])/2.0
	else:
		return merged[len(merged)//2]


# even - answe is 4.5
l1 = [1, 3, 5, 7, 9]
l2 = [0, 2, 4, 6, 8]
print(merge_sorted_lists(l1, l2))

# odd - answer is 5
l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8]
print(merge_sorted_lists(l1, l2))
