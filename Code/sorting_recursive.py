#!python
from sorting_iterative import insertion_sort


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
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
        #i is only one with elements remaining
        elif i < len(items1):
            sorted_items.append(items1[i])
            i += 1
        #j is ony one with elements remaining
        elif j < len(items2):
            sorted_items.append(items2[j])
            j += 1

    return sorted_items


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    mid = len(items) // 2

    items1 = items[0:mid]
    items2 = items[mid:]

    insertion_sort(items1)
    insertion_sort(items2)

    return merge(items1, items2)



def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

if __name__ == "__main__":
    items1 = [1, 3, 5, 7, 10]
    items2 = [2, 3, 9]
    items3 = [5, 1, 10, 6, 8, 2]
    print(merge(items1, items2))

    print(split_sort_merge(items3))