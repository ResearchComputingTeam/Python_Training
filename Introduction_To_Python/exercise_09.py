# Create a list 'a' with the elements 10, 21, 23, 11, and 24 in this order
a = [10, 21, 23, 11, 24]

# Modify the first element and the last element to be 0
a[0] = 0
a[-1] = 0

# Add the element 11 at the end of the list a
a.append(11)

# How many occurrences of 11 are there in a?
occurrences_of_11 = a.count(11)

# Extend the list a with another list ["foo", 4]
a.extend(["foo", 4])

# What is the location of the first occurrence of 11?
first_occurrence_index = a.index(11)

# Insert the value 100 as the third element
a.insert(2, 100)

# Remove the fourth element
del a[3]

# Remove the first occurrence of 11
a.remove(11)

# Convert non-integer elements to integers
a = [int(i) if isinstance(i, int) else i for i in a]

# Remove any non-integer elements from the list
a = [i for i in a if isinstance(i, int)]

# Sort the list
a.sort()

# Reverse the list
a.reverse()

# Compute the length of the resulting list
resulting_length = len(a)

# Print the resulting list and other information
print("Modified list:", a)
print("Number of occurrences of 11:", occurrences_of_11)
print("Location of the first occurrence of 11:", first_occurrence_index)
print("Length of the resulting list:", resulting_length)

