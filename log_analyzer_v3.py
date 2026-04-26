
file_path = input("\nPlease indicate the path to the file: ")
search_words = input("\nPlease enter search words: ")

list_words = [word.lower().strip() for word in search_words.split(",")]
found_words = {word: 0 for word in list_words}

line_count = 0

with open(file_path) as f:
    for line in f:
        line_lower = line.lower()
        is_found = False

        for word in found_words:
            if word in line_lower:
                count = line_lower.count(word)
                is_found = True
                found_words[word] += count

        if is_found:
            line_count += 1
            print(f"{line_count}. FOUND: {line}", end="")

print("\n--- Check completed ---")
print("\nTop results (sorted by occurrences):\n")

for i, (word, count) in enumerate(
    sorted(found_words.items(), key=lambda item: item[1], reverse=True), start=1
):
    print(f"{i}. {word:<10} → {count}")

print(f"\nTotal lines found: {line_count}")
