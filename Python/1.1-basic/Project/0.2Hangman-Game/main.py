import random
from hangman_arts import hangman_stages,logo
from hangman_words import word_list
print(logo[0])
chosen_word=(random.choice(word_list))


placeholder = ""
word_length = len(chosen_word)


for i in range(word_length):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letter=[]
stage = 0

while not game_over:
    print(f"**********************YOU HAVE {stage}/6 LEFT*********************")
    guess = input("Guess a letter from chosen word: ").lower()
    display = ""

    if guess in correct_letter:
        print(f"You already guessed letter${guess}")


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in correct_letter:
        print(hangman_stages[stage])
        stage += 1
        print(f"You guessed the letter {guess}.That is not in the chosen word.You lose a life")
        if stage == 6:
            game_over = True
            print(f"********************IT WAS ${chosen_word}! YOU LOSE*****************************")

    if "_" not in display:
        game_over = True
        print(f"************************YOU WIN**********************************")

    print(hangman_stages[stage])
