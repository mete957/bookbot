from collections import Counter
path_to_file = "books/frankenstein.txt"

def find_length(content):
    words = content.split()
    return len(words)

def find_frequency(content):
    frequency = Counter()
    for char in content:
        frequency[char.lower()] += 1    
    
    return dict(frequency)

def print_report(content):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{find_length(content)} words found in the document")
    for key,value in find_frequency(content).items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")

with open(path_to_file) as f:
    file_contents = f.read()
    
#print(find_length(file_contents))
#print(find_frequency(file_contents))
print_report(file_contents)
