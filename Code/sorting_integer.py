#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    #Find range of given numbers (minimum and maximum integer values)
    histogram = [0] * (max(numbers, default=0) + 1)

    #build histogram of counts
    for _, value in enumerate(numbers):
        histogram[value] += 1

    #Create output list
    index = 0
    for value, count in enumerate(histogram):
        while count > 0:
            numbers[index] = value
            index += 1
            count -= 1


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    #Get max value
    maximum = max(numbers, default=0) + 1

    #Init buckets
    buckets = list()
    for i in range(num_buckets):
        buckets.append(list())

    #Insert numbers into buckets
    for value in numbers:
        index = value * num_buckets // maximum
        buckets[index].append(value)

    #Mutate numbers
    index = 0
    for bucket in buckets:
        counting_sort(bucket)
        for item in bucket:
            numbers[index] = item
            index += 1
