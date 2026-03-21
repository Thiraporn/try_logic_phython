def bubble_sort(array):
    for sorted_inx in range(len(array) - 1):
        swapped = False
        for j in range(len(array) - sorted_inx - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swapped = True
        # Already Sorted
        if not swapped:
            break

    return array


unsort = [5, 4, 8, 3, 2, 0]
print(f'Sorted Array >> {bubble_sort(unsort)}')
