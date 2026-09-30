"""
Sorting Words with Custom Key Functions
This program demonstrates passing functions as arguments
"""

# Key function 1: Sort by word length
def sort_by_length(word):
    return len(word)


# Key function 2: Sort by lowercase version
def sort_by_lowercase(word):
    return word.lower()


# Key function 3: Sort by number of vowels (bonus)
def sort_by_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count


# Main sorting function that accepts a key function
def sort_words(word_list, key_function):
    """
    Sort a list of words using a custom key function.
    
    Args:
        word_list (list): List of words to sort
        key_function (function): Function that determines sort key for each word
    
    Returns:
        list: Sorted list of words
    """
    sorted_list = sorted(word_list, key=key_function)
    return sorted_list


# Test the functions
if __name__ == "__main__":
    words = ["Python", "apple", "Zebra", "banana", "Code", "xylophone"]
    
    print("Original list:", words)
    print("\n" + "="*50 + "\n")
    
    # Test 1: Sort by length
    print("Test 1: Sort by LENGTH")
    print("-" * 50)
    result1 = sort_words(words, sort_by_length)
    for word in result1:
        print(f"  {word:15} - length: {len(word)}")
    print("\nResult:", result1)
    
    print("\n" + "="*50 + "\n")
    
    # Test 2: Sort by lowercase
    print("Test 2: Sort by LOWERCASE (Alphabetical)")
    print("-" * 50)
    result2 = sort_words(words, sort_by_lowercase)
    for word in result2:
        print(f"  {word:15} - lowercase: {word.lower()}")
    print("\nResult:", result2)
    
    print("\n" + "="*50 + "\n")
    
    # Test 3: Sort by vowels (bonus)
    print("Test 3: Sort by NUMBER OF VOWELS (Bonus)")
    print("-" * 50)
    result3 = sort_words(words, sort_by_vowels)
    for word in result3:
        vowel_count = sum(1 for letter in word if letter in "aeiouAEIOU")
        print(f"  {word:15} - vowels: {vowel_count}")
    print("\nResult:", result3)
    
    print("\n" + "="*50 + "\n")
    
    # Interactive test
    print("TEST WITH USER INPUT")
    print("-" * 50)
    user_input = input("Enter words separated by spaces: ")
    user_words = user_input.split()
    
    if user_words:
        print("\nOriginal:", user_words)
        print("Sorted by length:", sort_words(user_words, sort_by_length))
        print("Sorted alphabetically:", sort_words(user_words, sort_by_lowercase))
