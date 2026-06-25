'''implement selection sort'''

'''IDEA --> 2 parts - sorted and unsorted, iterate the unsorted array, find the largest (or smallest if descending order) element
from the unsorted array and place it in the sorted array. '''

# MY WAY - 2 parts - sorted and unsorted. As the name suggests, I need to select the largest element from the unsorted array and place it in the sorted array.
# there will be sorted and unsorted array. Keep on finding the largest element from the unsorted array and placing it in the sorted array till the array does not gets sorted


def selection_sort(arr):
    n = len(arr) 
    j = n-1     
    for _ in range(n-1):
        max_index = j
        for i in range(j):
            if arr[i]>arr[max_index]:
                max_index = i
        arr[max_index], arr[j] = arr[j], arr[max_index]
        j -=1

arr = [5, 3, 2, 1, 6, 2, -1, 0, 1]      
print("unsorted arr: ", arr)
selection_sort(arr)
print("sorted array: ", arr)


# TIME COMPLEXITY - O(n^2) where n = size of the array
            # BEST CASE = AVG CASE = WORST CASE --> O(n^2)
# SPACE COMPLEXITY - O(1) - no extra space required, just the normal variables.
# STABLE - NO -> the order of the same elements gets changed after sorting--> equal elements can change relative order. 
#In-place swapping --> no extra space required for sorting

