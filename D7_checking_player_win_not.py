import random

print("Welcome to guess word ")
wordlist = ["apple","camel","doggy","water"]

chosen_word = random.choice(wordlist)
print(chosen_word)

placeholder = ""
wlen = len(chosen_word)
for position in range(wlen):
    placeholder += "_"
print(placeholder)

game_over = False
current_letter = []
while not game_over:
    guess = input("Guess a letter : ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            current_letter.append(guess)
        elif letter in current_letter:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You Win")






















