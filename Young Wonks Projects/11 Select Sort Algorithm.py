#11 select sort
# algorithm repeatedly finds the min element from the list and puts
# it at the beginning of the list - swaps smallest element and element at
# beginning of the list

#swapper code
##temporary = a
##a = b
##b = a

A = [7,3,6,1,2,4]
print("list before ",A)
j=0

for j in range(len(A)):
    min_index = j

    #other index is the index that will be swapped with min_index

    value=A[min_index]
    for i in range(j,len(A)):
        if A[i] < value:
            min_index = i
            value =A[i]
    print(min_index, A[min_index])


    temporary = A[min_index]
    A[min_index] = A[j]
    A[j] = temporary
print("list after ",A)
