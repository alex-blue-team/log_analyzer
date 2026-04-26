# LOG ANALYZER v2.1
# This tool searches for multiple keywords inside a выбранного пользователем лог-файла
# and prints matching lines (each line counted only once)


# --- TOOL HEADER ---
print("\n--- LOG ANALYZER ---\n")

# --- USER INPUT: FILE PATH ---
file_path = input("Enter path to log file: ")

# --- USER INPUT: KEYWORDS ---
key_words = input("\nEnter search words separated by commas: ")

list_words = [word.strip().lower() for word in key_words.split(",")]

found_line = 0

print()



with open(file_path) as f:
    # Loop through each line in the file
    for line in f:
        line_lower = line.lower()

        # Check each keyword
        for word in list_words:
            # If keyword is found inside the line
            if word in line_lower:
                found_line += 1
                print(f"[{found_line}] FOUND: {line.strip()}")
                break  # stop checking other words for this line

# --- FINAL OUTPUT ---
print("\nCheck completed")

if found_line > 0:
    print(f"{found_line} logs found matching your words")
else:
    print("The search terms were NOT found")
