#==============================================
# STRINGS
# - Strings are immutable in python
# - If modifying a string, a new string will need to be made, O(n)
#==============================================
s = "Hello"

#append to the end of the string O(n)
b = s + "z"
print("Appended-" + str(b))

#length of string O(1)
print("Length of String-" + str(len(s)))

#check if in string O(n)
if "o" in s:
    print("Check if in string-" + str(True))

#accessing an element at an index O(1)
print("Accessing-"+ s[0])