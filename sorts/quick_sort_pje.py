def quick_sort_pje(sorting, left, right):
	if left >= right:
		return

	i = left + 1
	j = right

	while i < j:
		while i <= j and sorting[i] <= sorting[left]:
			i += 1
		while j >= i and sorting[j] >= sorting[left]:
			j -= 1
		if i <= j:
			sorting[i], sorting[j] = sorting[j], sorting[i]
		else:
			sorting[left], sorting[j] = sorting[j], sorting[left]

	quick_sort_pje(sorting, left, j - 1)
	quick_sort_pje(sorting, j + 1, right)

if __name__ == '__main__':
    unsorted = [12, 23, 4, 5, 3, 2, 12, 81, 56, 95]
    quick_sort_pje(unsorted,0,len(unsorted)-1)
    print(unsorted)
