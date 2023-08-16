
# Study of the insertion sort algorithm. Originated from the late 1940s


def insertSort(arr):
    for i in range(1, len(arr)): #-The for loop is used as a reference point. From this point, the possible inequality of the numbers 
                                  #prior are checked. The swapping of pairs keeps going backwards in position until it is in ascending order.
                                   #If the numbers are in ascending order prior to the reference point (i), the point moves forward by one
                                   #and the algorithm continues onwards!
        j = i - 1                #-i parses the natural numbers, j parses the index numbers. i will be j+1 in index notation.
                                   #It will reset to be the current reference point at the start of every for loop.
        while j >= 0 and arr[i] < arr[j]: #-while: For all pairs prior to the reference point, keep swapping while the number in front is smaller 
                                        #than the one behind it. (i.e. arr[i] < arr[j])
                                        #-'j >= 0' to avoid the index-out-of-range error. 'i >= 1' is another alternative.
            arr[j], arr[i] = arr[i], arr[j] #-Swap the pair if the condition is met.
            i -= 1                       #-The recursive property! Scan the pairs backwards from the reference point i.
            j -= 1 
                                 #-The while loop exits once the numbers are ascending up to the reference point i. Back to the for loop!
    return arr                   


l = [2, 3, 6, 1, 2, 4, 7, 2, 13, 8]
result = insertSort(l)
print(result)





        

