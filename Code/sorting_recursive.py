#!python
from sorting_iterative import insertion_sort, bubble_sort, swap


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n + m) where n and m are passed in arrays
    Memory usage: O(n + m) where n and m are the number of elements in each array"""
    sorted_items = []

    i = 0
    j = 0
    while i < len(items1) or j < len(items2):

        #items are both in bounds
        if i < len(items1) and j < len(items2):
            if items1[i] < items2[j]:
                sorted_items.append(items1[i])
                i += 1
            else:
                sorted_items.append(items2[j])
                j += 1
        else:
            #i is only one with elements remaining
            if i < len(items1):
                sorted_items.extend(items1[i:])
            #j is ony one with elements remaining
            else:
                sorted_items.extend(items2[j:])

            break

    return sorted_items


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    mid = len(items) // 2

    items1 = items[:mid]
    items2 = items[mid:]

    bubble_sort(items1)
    bubble_sort(items2)

    items[:] = merge(items1, items2)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    mid = len(items) // 2

    #base case
    if len(items) > 1:

        #divide items
        items1 = items[:mid]
        items2 = items[mid:]

        #call merge sort
        merge_sort(items1)
        merge_sort(items2)

        #begin merging after calls reach base case
        items[:] = merge(items1, items2)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot with median of 3 function from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    mid = (low + high) // 2
    pivot = mid

    #choose pivot
    if items[mid] < items[high] and items[mid] > items[low]:
        pivot = mid
    elif items[low] < items[mid] and items[low] > items[high]:
        pivot = low
        swap(items, items[low], items[mid])
    elif items[mid] < items[high]:
        pivot = high
        swap(items, items[high], items[mid])
        
    left = low
    right = high

    #choose piviot
    #left reference to lowest
    #right reference to highest
    while left < right:
        #find item greater than pivot
        while items[left] < items[pivot]:
            left += 1

        #find item less than pivot
        while items[right] > items[pivot]:
            right -= 1

        #swap items
        if items[left] > items[pivot] and items[right] < items[pivot]:
            swap(items, left, right)
            left += 1
            right -= 1

        #Move pivot to final position
        if left >= right:
            swap(items, left, pivot)
            return pivot

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    #start quicksort
    if low == None and high == None:
        quick_sort(items, low = 0, high = len(items) - 1)


    #Base case input is too small
    if len(items) == 1 or high - low <= 1:
        return

    #partition items
    pivot = partition(items, low, high)

    #sort left sublist
    if low < pivot:
        quick_sort(items, low, pivot)
    
    #sort right sublist
    if right > pivot:
        quick_sort(items, pivot, right)

if __name__ == "__main__":
    items1 = [1, 3, 5, 7, 10]
    items2 = [2, 3, 9]
    items3 = [5, 1, 10, 6, 8, 2]
    print(merge(items1, items2))

    print(split_sort_merge(items3))