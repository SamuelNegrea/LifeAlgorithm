import time

def print_flat_earth_measures():
    measures = {
        "Equator Line Circumference": "63,252.58 Kms or 39,303.33 Mi",
        "Diameter of the Equator Line": "20,133.92 kms or 12,510.64 Mi",
        "Diameter of the Flat Earth (Antarctic Borders)": "40,267.84 Kms or 25,021.28 Mi",
        "Radius of the Equator (North Pole x Equator Line)": "10,066.96 kms or 6,255.32 Mi",
        "Radius of the Flat Earth (North Pole x Parallel 90°S)": "20,133.92 kms or 12,510.64 Mi",
        "Antarctic Borders (Ice Wall) Parallel 90°S Circumference": "126,505.1718 kms or 78,606.67 Mi"
    }

    title = "THE REAL MEASURES OF THE EARTH"
    print(title)
    print()
    for description, value in measures.items():
        print(f"{description}: {value}")
        print()

# Call the function to print the measures
print_flat_earth_measures()

time.sleep(5)

# Define the mapping from letters to numbers
letter_to_number = {
    'A': 26, 'B': 25, 'C': 24, 'D': 23, 'E': 22, 'F': 21, 'G': 20, 'H': 19, 'I': 18, 'J': 17, 'K': 16, 'L': 15, 
    'M': 14, 'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1
}


RED = '\033[91m'
RESET = "\033[0m"
GREEN = "\033[92m"

print()


# Function to calculate the sum of a word and print each letter with a delay
def print_word_with_delay(word):
    for letter in word:
        print(f"{RESET}{letter}: {GREEN}{letter_to_number[letter]}{RESET}")
        time.sleep(0.1)  # 100ms delay

# Words to print
words = ["NATIONAL", "AERONAUTICS", "AND", "SPACE", "ADMINISTRATION"]


# Print each letter in each word with the delay
for word in words:
    print(f"Word: {word}")
    print_word_with_delay(word)
    print()  # Add an empty line between words

# Function to calculate the sum of a word
def calculate_word_sum(word):
    return sum(letter_to_number[letter] for letter in word)


values = {word: calculate_word_sum(word) for word in words}

# Print the values
for word, value in values.items():
    print(f"{RESET}{word}: {value}")
    time.sleep(0.7)  # 100ms delay

# Calculate the total sum
total_sum = sum(values.values())
print(f"\nTotal Sum: {RED}{total_sum}{RESET}")
print()
