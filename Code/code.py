#for each item in array
    #if item is not less than or equal to item + 1 and not out of bounds
        #return false
#return true


#[1,5,9,6]

#1,6,3,4,9

a = [1, 6, 3, 5, 9, 7]

def bubble_sort(a):
    for i in range(a - i):
        for j in range(a - i):
            if a[i] > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
                swapped = True
        if not swapped:
            return a
    return a


if __name__ == "__main__":
    pass

#for item in remaining length of array
    #for item in remaining length of array
        #if item is greater than item+1
            #swap item and item+1

    #length remaining--