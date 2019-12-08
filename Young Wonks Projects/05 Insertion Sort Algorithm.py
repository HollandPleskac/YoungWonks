#05 insertion sort
#opens spaces in a list to insert number

#this code swaps two numbers - A[j] and A[j-1]
##temporary = A[j]
##A[j] = A[j-1]
##A[j-1] = temporary

A = [2,1,6,3,10,4]
i = 1
while i < len(A):
    j=i
    while j > 0 and A[j-1]>A[j]:
        temporary = A[j]
        A[j] = A[j-1]
        A[j-1] = temporary
        j = j-1
        
    i = i+1

print(A)
