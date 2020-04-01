#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(N) - Iterates over the entire array - 1
    Memory usage: O(N) - No extra space allocated. Only the array"""
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True
        
def swap(items, i, j):
    tmp = items[i]
    items[i] = items[j]
    items[j] = tmp

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Worst Case O(N^2) - reverse order Best Case O(N) - sorted array
    Memory usage: ??? Why and under what conditions?"""
    for i in range(len(items)):
        swapped = False
        for j in range(len(items) - i - 1):
            #compare and swap
            if items[j] > items[j + 1]:
                swap(items, j, j+1)
                swapped = True
        #No elements swapped - already sorted
        if swapped == False:
            return


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: Worst Case O(N^2) - reverse order Best Case O(N^2) - sorted algorithm still does N^2 passes
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(len(items)):
        min_index = i
        for j in range(i, len(items)):
            if items[j] < items[min_index]:
                min_index = j

        swap(items, i, min_index)


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
