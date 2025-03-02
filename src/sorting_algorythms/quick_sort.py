def partition(arr, low, high):
	i = (low - 1)		 # index of smaller element
	pivot = arr[high]	 # pivot

	for j in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot:

			# increment index of smaller element
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1


def quick_sort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:

		pi = partition(arr, low, high)
		quick_sort(arr, low, pi - 1)
		quick_sort(arr, pi + 1, high)
