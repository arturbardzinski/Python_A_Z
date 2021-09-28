

lives = 5
word = "artur"
used_letters = []
user_word = []

def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes
for _ in word:
    user_word.append("_")

while True:
    letter = input("Podaj literę: ")
    used_letters.append(letter)

    print(word.index(letter))
    print(f"Użyte liter: {used_letters}")