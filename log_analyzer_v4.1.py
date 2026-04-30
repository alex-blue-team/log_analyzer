# Mini Log Analysis Tool (v4.1)
# This tool scans a log file and counts exact matches of user-defined words.
# It also tracks how many lines contain those words and displays sorted results.

# Ask user for file path and search words
file_path = input("\nSpecify the path to the required file: ")
search_words = input("\nEnter search words: ")

# Convert input string into a list of clean, lowercase words
list_words = [word.lower().strip() for word in search_words.split(",")]

# Create a dictionary to store word counts
found_words = {word: 0 for word in list_words}

# Counter for lines where at least one word was found
counted_lines = 0

# Open the file and process it line by line
with open(file_path) as f:
    for line in f:
        formatted_line = line.lower().split()

        is_found = False

        for word in found_words:
            # Count exact matches of the word in the current line
            count_word = formatted_line.count(word)

            if count_word > 0:
                is_found = True
                found_words[word] += count_word

        # If at least one word was found — print the line
        if is_found:
            counted_lines += 1
            print(f"{counted_lines}. FOUND: {line}", end="")

print("\n---- Check completed ----\n")

# Sort results by frequency (highest first) and print them
for i, (word, count) in enumerate(
    sorted(found_words.items(), key=lambda item: item[1], reverse=True), start=1
):
    print(f"{i}. {word:<10} → {count}")

print(f"\nTotal line found: {counted_lines}")
