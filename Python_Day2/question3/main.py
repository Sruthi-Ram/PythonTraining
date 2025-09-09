from utilities import string_ops, math_ops, file_ops

text = input("Enter text: ")
cleaned = string_ops.remove_punctuation(text)
vowel_count = string_ops.count_vowels(cleaned)
print("Cleaned text:", cleaned)
print("Vowel count:", vowel_count)

numbers = list(map(float, input("Enter numbers separated by space: ").split()))
print("Mean:", math_ops.mean(numbers))
print("Median:", math_ops.median(numbers))
print("Standard Deviation:", math_ops.standard_deviation(numbers))

filename = input("Enter filename to write: ")
file_ops.write_file(filename, cleaned)
print("File written.")

keyword = input("Enter keyword to search in file: ")
found = file_ops.search_in_file(filename, keyword)
print("Keyword found:", found)
