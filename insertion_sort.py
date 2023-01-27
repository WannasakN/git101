def insertion_sort(a):
	if (n := len(a)) <= 1:
	return
	for i in range(1, n):		
		key = a[i]
		j = i-1
		while j >=0 and key < a[j] :
				a[j+1] = a[j]
				j -= 1
		a[j+1] = key

a = [12, 11, 13, 5, 6]
insertion_sort(a)
print(a)
