
#==============================================
# ARRAYS
# When a static array needs to insert at end:
#   - Array size will be doubled
#   - Item will be inserted
#   - If double required, O(n)
#   - If double previously done and there's space O(1)
# When a static array needs to insert in the middle
#   - Array size doubled, all elements shifted to the right
#   - Item placed in new open position
# When a static array deletes an item in the middle O(n)
#   - All elements need to be shifted to the left to keep contiguous memory
# When deleting (popping) at the end O(1)
#   - Item deleted at end, extra space stays for future inserting
#==============================================

A = [1, 2, 3, 4, 5]
print(A)

#Append to the end of the array *O(1), sometimes O(n)
A.append(6)
print("Appended-" + str(A))

#Popping from end O(1)
A.pop()
print("Popped-" + str(A))

#insertion not at end O(n)
A.insert(1, 7)
print("Inserted-" + str(A))

#deletion not from end O(n)
A.pop(2)
print("Popped-" + str(A))

#modifying an element O(1)
A[0] = 9
print("Updated-" + str(A))

#random access O(1)
print("Random Access-"+str(A[0]))

#checking if element exists O(n)
if 9 in A:
    print("If in array-"+str(True))

#checking length of the array O(1), property of length saved, dont have to loop through
print("Length of Array-"+str(len(A)))