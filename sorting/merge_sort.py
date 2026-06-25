'''implement merge sort'''

'''IDEA --> Divide & Conquer
Keep on dividing the array repeatedly until all the elements are separated - because a single element is always sorted.
Then Merge the divided arrays in a way that they combine in the sorted way. On combining, it is sure that both the divided parts are
sorted as a whole when just considered them as individual arrays.'''


# Merge Sort follows the Divide and Conquer paradigm.
# The array is recursively divided into two halves until each subarray contains only one element.
# Since a single element is already sorted, the divided subarrays are then merged back together in sorted order.
# During merging, two already sorted subarrays are combined to form a larger sorted subarray.
# This process continues until the entire array becomes sorted.


def merge(arr, start, end, mid):
    result = []
    start1 = start
    start2 = mid+1
    while start1<=mid and start2 <=end:
        if arr[start1]<=arr[start2]:
            result.append(arr[start1])
            start1+=1
        else:
            result.append(arr[start2])
            start2 += 1
    while start1<= mid:
        result.append(arr[start1])
        start1 += 1
    while start2<= end:
        result.append(arr[start2])
        start2 += 1
    
    arr[start: end+1] = result

def merge_sort(arr, start, end):
    if start<end:
        mid = start + (end-start)//2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, end, mid)

# arr = [5, 3, 2, 1, 6, 2, -1, 0, 1]
arr = [1,2,3,4,4]
print("unsorted arr: ", arr)
merge_sort(arr, 0, len(arr)-1)
print("sorted array: ", arr)


# TIME COMPLEXITY - O(n*logn) where n = size of the array
            # BEST CASE = AVG CASE = WORST CASE --> O(n*logn)

# SPACE COMPLEXITY - O(n) - extra space is required
                # Auxiliary Array = O(n)
                # Recursion Stack = O(log n)
                # total = O(n)

# STABLE - YES -> maintains the order of the elements after sorting -> relative order of the same elements is maintained
# No In-place swapping -- extra memory is required  --> An algorithm is in-place if it uses only O(1) extra memory.