import random

#
#open the text file in read mode
#
def load_word():
    #here we use words.txt sourced from https://github.com/Xethron/Hangman/blob/master/words.txt
    with open("words.txt", "r") as file:
        #read all the lines in the file
        allText = file.read()
        #split the words in the file
        words = list(map(str, allText.split()))
        #select a random word from the list of words
        word = random.choice(words)
        return word

#
#print image from spaceman-display.txt based on the number of failed attempts
#
def print_image(attempts):
    with open("spaceman-display.txt", "r") as file:
        line = file.readlines()
        #print the image based on the number of failed attempts
        #the image is stored in 3 line segments
        print(line[3*(7-attempts)].rstrip())
        print(line[3*(7-attempts)+1].rstrip())
        print(line[3*(7-attempts)+2].rstrip())

#
#check if the letter in the secret word is in the list of letters guessed
#
def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

#
#create a string to store the guessed word
#
def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    #check if the letter in the secret word is in the list of letters guessed
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_"
    return guessed_word

#
#create a string to store the available letters
#
def get_available_letters(letters_guessed):
    available_letters = ""
    #check if the letter in the secret word is in the list of letters guessed
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters


#
#gameplay loop
#
def spaceman(secret_word):

    #into message
    print("I am thinking of a word that is", len(secret_word), "letters long: ", get_guessed_word(secret_word, ""))
    print("-------------")

    letters_guessed = []
    attempts = 7

    #main game loop
    while attempts > 0:

        #check if the word is guessed
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            break
        
        #print the image, available letters, and prompt the user to guess a letter
        print_image(attempts)
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()

        #check if the letter is in the secret word
        if guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            attempts -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

        print("-------------")
        
    #check if the player ran out of attempts    
    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", secret_word)

#load the secret word and start the game
secret_word = load_word()
spaceman(secret_word)
