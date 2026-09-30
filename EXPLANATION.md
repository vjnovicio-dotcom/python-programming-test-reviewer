# Text Formatting Program - Detailed Explanation

## What Does This Program Do?

This program takes messy text and cleans it up. It does 3 things:
1. **Removes extra spaces** - eliminates multiple spaces between words
2. **Capitalizes sentences** - makes the first letter of each sentence uppercase
3. **Counts words** - tells you how many words are in the text

### Example:
**Input:** `"  hello   world.  how   are you?  "`
**Output:** `"Hello world. How are you?"` with `4` words

---

## Understanding Each Function

### Function 1: `remove_extra_spaces(text)`
**Purpose:** Clean up spacing in text

**What it does:**
- Removes spaces at the start and end using `.strip()`
- Replaces all double spaces with single spaces
- Keeps repeating until no double spaces remain

**Example:**
```
Input:  "  hello   world  "
Output: "hello world"
```

---

### Function 2: `capitalize_sentences(text)`
**Purpose:** Capitalize the first letter after sentence endings

**What it does:**
- Starts by assuming we need to capitalize (first word)
- Goes through each character one by one
- If it's a letter AND we need to capitalize, make it UPPERCASE
- If we find a `.`, `?`, or `!`, mark that we need to capitalize the next letter

**Example:**
```
Input:  "hello world. how are you?"
Output: "Hello world. How are you?"
```

---

### Function 3: `count_words(text)`
**Purpose:** Count total words in the text

**What it does:**
- Splits the text by spaces (`.split()`)
- This creates a list of words
- Returns the length (number of items in the list)

**Example:**
```
Input:  "hello world"
Output: 2
```

---

### Function 4: `format_text(text)` - The Coordinator
**Purpose:** Run all functions in the RIGHT order

**Steps (in order):**
1. Call `remove_extra_spaces()` to clean spacing
2. Call `capitalize_sentences()` on the cleaned text
3. Call `count_words()` to count
4. Return both the formatted text AND the count

---

## Key Concepts Used

| Concept | Example |
|---------|---------|
| **Functions** | `def remove_extra_spaces(text):` |
| **Strings** | `"hello world"` |
| **String Methods** | `.strip()`, `.replace()`, `.split()`, `.isalpha()` |
| **Loops** | `while` and `for` loops |
| **Control Flow** | `if` statements |
| **Lists** | `text_list = list(text)` converts string to list |
| **Tuples** | `return formatted_text, word_count` returns a tuple |

---

## Common String Methods Explained

```python
text = "  hello world  "

text.strip()           # Removes spaces at start and end
# Result: "hello world"

text.replace("a", "b") # Replaces all "a" with "b"
# Result: "  hello world  " (no 'a' to replace)

text.split()           # Splits by spaces into a list
# Result: ['hello', 'world']

"h".isalpha()          # Checks if character is a letter
# Result: True

"h".upper()            # Converts to uppercase
# Result: 'H'
```
