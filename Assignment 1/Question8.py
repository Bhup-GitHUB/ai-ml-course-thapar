# 8. Dictionaries
# Create a dictionary to store student names and their grades. Display the highest and lowest grades.
# Count the occurrences of each word in a sentence.
# Merge two dictionaries and sort the result by keys

student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
highest_grade = max(student_grades.values())
lowest_grade = min(student_grades.values())
print("Highest grade:", highest_grade)
print("Lowest grade:", lowest_grade)
def word_occurrences(sentence):
    words = sentence.split()
    occurrences = {}
    for word in words:
        if word in occurrences:
            occurrences[word] += 1
        else:
            occurrences[word] = 1
    return occurrences
sentence = input("Enter a sentence: ")
print("Word occurrences:", word_occurrences(sentence))
def merge_sort_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  
    merged_dict.update(dict2)
    sorted_dict = dict(sorted(merged_dict.items())) 
    return sorted_dict
dict1 = {"a": 1, "c": 3}
dict2 = {"b": 2, "d": 4}
merged_sorted = merge_sort_dictionaries(dict1, dict2)
print("Merged and sorted:", merged_sorted)