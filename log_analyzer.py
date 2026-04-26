

# Simple log analyzer for SOC practice
# Searches for a keyword in system logs and counts occurrences

key_word = input("Enter the word you want to search for: ")

count_line = 0 


# with open ("/var/log/auth.log") as f:   Here I will connect different files
with open ("/var/log/syslog") as f:
        for line in f:
                if key_word.lower() in line.lower():
                        count_line +=1
                        print(f"{count_line}. FOUND: {line.strip()}")

print("\nCheck completed")

if count_line > 0:
        print(f"{count_line} logs found matching the word {key_word.upper()}")
else:
        print("The search terms were NOT found")
