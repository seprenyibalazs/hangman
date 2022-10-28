import random
from hangman_words import word_list
from hangman_art import emblema, stages
lista = word_list
choosen = random.choice(lista)
print(emblema)
print(f"The choosen word is: {choosen}")

lives = 6


display = []

word_lengt = len(choosen)
for _ in range(word_lengt):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    ask = input("Guess a letter: ").lower()

    if ask in display:
        print(f"You've already guessed {ask} !")

    for position in range(word_lengt):
        letter = choosen[position]
        if letter == ask:
            display[position] = ask
    if ask not in choosen:
        lives -= 1
        print(f"your guessed {ask}, is not the word. you lost a life.")
        if lives == 0:
            end_of_game = True
            print("you lose")

    print(display)

    if "_" not in display:
        end_of_game == True
        break
        print("you win")
    print(stages[lives])
