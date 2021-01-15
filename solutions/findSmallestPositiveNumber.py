def findSmallestPositiveNumber(l):
    smallest = float('inf')

    for n in l:
        if n < smallest and n >= 0:
            smallest = n
    
    return smallest