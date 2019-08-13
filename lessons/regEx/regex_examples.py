import re


text = "today i got to work early"

# Search the string to see if it starts with "today" and ends with "early"
x = re.search(r"^today.*early$", text)
print(x)

# Print a list of all matches
x = re.findall(r"to", text)
print(x)

# Return an empty list if no match was found
x = re.findall(r"zombie", text)
print(x)

# Search for the first white-space character in the string
x = re.search(r"\s", text)
print("The first white-space character is located in position:", x.start())

# Make a search that returns no match
x = re.search(r"boni", text)
print(x)

# Split at each white-space character
x = re.split(r"\s", text)
print(x)

# Split the string only at the first occurrence
x = re.split(r"\s", text, 1)
print(x)

# Replace every white-space character with the number 9
x = re.sub(r"\s", "9", text)
print(x)

# Replace the first 2 occurrences
x = re.sub(r"\s", "9", text, 2)
print(x)

# Do a search that will return a Match Object
x = re.search(r"go", text)
# The Match object has properties and methods
# used to retrieve information about the search, and the result:
#
#   .span() returns a tuple containing the start-, and end positions of the match.
#   .string returns the string passed into the function
#   .group() returns the part of the string where there was a match
print(x)

# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with a "w"
x = re.search(r"\bw\w+", text)
print(x.span())

# Print the string passed into the function
x = re.search(r"\bS\w+", text)
print(x.string)

# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with a "w"
x = re.search(r"\bS\w+", str)
print(x.group())
