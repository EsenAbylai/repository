## Strings

# Mandatory problems:


# String Concatenation:
# Concatenate the strings 'Python', 'is', 'a', 'powerful', 'language' to create a single string, 'Python is a powerful language.'

python = "Python"
isa = "is"
a = "a"
powerful = "powerful"
print(f"{python} {isa} {a} {powerful}")

# Variable Declaration:
# Declare a variable named topic and assign it the value "strings in Python."

variable = "strings in Python."
print(variable)

# Printing with Escape Symbols:
# Print the following sentence, including the double quotes: "Learning about "Python" strings is fun."

variable = "Learning about 'Python' strings is fun."
print(variable)

# String Length and Character Count:
# Calculate and print the length of the topic string. Also, count and print how many times the letter 's' appears in the string.
variable = "Learning about 'Python' strings is fun."
variable_l = variable.len()
print(variable.count('s'))
print(variable_l)

# Uppercase and Lowercase Conversion:
# Create a new variable called upper_topic by converting the topic string to uppercase. Then, create another variable called lower_topic by converting the topic string to lowercase.

upper_topic = "topic"
print(upper_topic.lower())

upper_topic = "topic"
print(upper_topic.upper())

# String Formatting:
# Use f-strings to format the topic string in the following way: "Let's learn about {topic}."
upper_topic = "topic"
print(f"Let's learn about {upper_topic}.")

# Substring Extraction:
# Extract and print the word 'Python' from the topic string.

variable = "strings in Python."
print(variable[11:])

## Bonus problems


# Substring Search:
# Check if the topic string contains the word 'Python' using the in keyword.

variable = "strings in Python."
print("Python" in variable)

# String Replacement:
# Replace the word 'Python' in the topic string with 'programming' and print the modified string.

variable = "strings in Python."
print(variable.replace('Python', 'programming'))


# String Splitting:
# Split the string 'Python,Java,C++,Ruby' into a list of programming languages using a comma as the separator.

programming = "Python,\tJava,\tC++,\tRuby"
print(programming)


# Character at Index:
# Find and print the character at index 4 in the topic string.

upper_topic = "topic"
print(upper_topic[4])

# String Repetition:
# Create a new string that repeats the word 'Python' three times, separated by hyphens.

new_string = 'Python Python Python'
string = " - ".join(new_string.split())
print(string)


# Escape Symbols in String:
# Create a string that contains a newline character to print the following text on separate lines:
# Hello,
# World!

my_string = "Hello,\nWorld!"
print(my_string)

# String Capitalization:
# Capitalize the first letter of each word in the string 'python programming is amazing.'

original_string = 'python programming is amazing.'
print(original_string.title())

# String Removal and Trimming:
# Remove any leading or trailing whitespace from the string '  Python For All ' and print the trimmed result.

original_string = '  Python For All '
print(original_string.strip())







## Lists

## Mandatory problems:


# List Append and Extend:
# Create a list called programming_languages with the elements . Use the append() method to add 'C++' to the list. Then, use the extend() method to add ['JavaScript', 'Ruby'] to the list. Print the updated list.

programming_languages = ['Python', 'Java']
programming_languages.append('C++')
print(programming_languages)


# List Insertion:
# Insert the string 'C#' at the third position in the programming_languages list and print the modified list.

programming_languages = ['Python', 'Java', 'C++']
programming_languages.insert(2, 'C#')
print(programming_languages)

# List Removal:
# Remove the second element from the programming_languages list and print the updated list.

programming_languages = ['Python', 'Java', 'C#', 'C++']
programming_languages.pop(1)
print(programming_languages)

