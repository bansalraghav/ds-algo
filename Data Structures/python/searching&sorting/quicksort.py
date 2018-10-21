"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array):
    counter = 0
    l = len(array)
    if l < 2:
        return array
    else:
        pivot = array[l-1]
        less = [i for i in array[:l-1] if i <= pivot]
        greater = [i for i in array[:l-1] if i > pivot]
        print counter
        return quicksort(less) + [pivot] + quicksort(greater)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
