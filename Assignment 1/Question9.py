# 9. File Handling
# Write data to a file and then read it back.
# Count the number of lines, words, and characters in a text file.
# Append new data to an existing file without overwriting.


file = open("my_file.txt", "w")
file.write("Hello, file!\nThis is some data.")
file.close()

file = open("my_file.txt", "r")
content = file.read()
file.close()

print("File content:\n", content)

# Count lines, words, characters
def file_stats(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    num_lines = len(lines)
    num_words = 0
    num_chars = 0

    for line in lines:
        num_words += len(line.split())
        num_chars += len(line)

    return num_lines, num_words, num_chars

lines, words, chars = file_stats("my_file.txt")
print("Lines:", lines, "Words:", words, "Characters:", chars)

# Append to file
file = open("my_file.txt", "a")
file.write("\nAppended data.")
file.close()

file = open("my_file.txt", "r")
print("Appended file:\n", file.read())
file.close()