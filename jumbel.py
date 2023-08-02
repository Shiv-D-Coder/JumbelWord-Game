# jumble Game
import random
import time
import emoji
import colorama
from colorama import Back, Fore, Style

# List of words to choose from
word_list = ["father", "enterprise", "science", "programming", "resistance", "fiction",
             "condition", "reverse", "computer", "python"]

# Choose a random word from the list
choose = random.choice(word_list)

# Convert the chosen word into a list
jumble = list(choose)

# Shuffle the letters in the list to create a jumbled word
random.shuffle(jumble)

# Convert the shuffled list back to a string
jumbled_word = ''.join(jumble)

# Print the jumbled word to the user
print("Jumbling the word for you...")
time.sleep(2)
print(f"JUMBLED word is {Fore.CYAN}{Style.BRIGHT}{jumbled_word}")

# Start the game loop
while True:
    # Ask the user to enter their guess
    word = input(f"{Fore.BLUE}Please, enter the correct word: ")
    print("Matching your answer, please wait")
    time.sleep(0.5)
    
    # Check if the guessed word is correct
    if word != choose:
        print(f"{Fore.RED}{word} is not correct, please try again", end="")
        print(emoji.emojize(":pensive_face:") * 2)
        word = input("Please, enter the correct word: ")
    
    # If the guessed word is correct, end the game loop and print a congratulatory message
    if word == choose:
        print(f"{Fore.GREEN}{Style.BRIGHT}Congratulations {word} is the right word!", end="")
        print(emoji.emojize(":partying_face:") * 2)
        break
