import random
import hangman_pic

word = ''
word_length = 0
words = []
current_progress = []
loose_count = 0
win_count = 0
wrong_guesses = []

def menu():
    str_input = input("Enter 'S' for start, 'P' for previous words, 'E' for exit... \n").upper()

    if str_input == 'S':
        start_game()
    elif str_input == 'P':
        previous_words()
    elif str_input == 'E':
        exit()
    else:
        print("Wrong input \n")
        menu()

def start_game():
    global word
    global word_length
    global current_progress

    word = random.choice(words)
    write_used_words(word)

    word_length = len(word)
    current_progress = list("_ " * word_length)

    print("The word to guess: %s" % "".join(current_progress))
    input_guess_option()

def read_words():
    global words

    with open('hangman/words.txt', 'r') as f:
        words = f.read().split('\n')

def write_used_words(word):
    with open('hangman/used_words.txt', 'a') as f:
        f.write(word + '\n')

def previous_words():
    print("Previous words:\n")
    with open('hangman/used_words.txt', 'r') as f:
        print(f.read())
    menu()

def restart():
    global loose_count
    global win_count
    global current_progress

    loose_count = 0
    win_count = 0

    menu()

def input_guess_option():
    str_input = input("Guess a letter or the whole word: ").lower()
    if len(str_input) == 0:
        input_guess_option()
    elif len(str_input) > 1:
        guess('W', str_input)
    else:
        guess('L', str_input)

def guess(option, input):
    if option == 'L':
        refresh_by_letter(input)
    if option == 'W':
        refresh_by_word(input)

    check_state()

def refresh_by_letter(letter):
    global current_progress
    global win_count
    global loose_count

    guessed = False

    for i in range(word_length):
        if word[i] == letter:
            current_progress[i*2] = letter
            win_count += 1
            guessed = True

    if not guessed:
        loose_count += 1
        wrong_guesses.append(letter)

def refresh_by_word(word_guess):
    global current_progress
    global win_count
    global loose_count

    if word_guess == word:
        win_count = word_length
        for i in range(word_length):
            current_progress[i*2] = word[i]

    else:
        loose_count += 1
        wrong_guesses.append(word_guess)

def print_current_progress():
    hangman_pic.render_pic(loose_count, word_length)

    print("Current progress: %s" % "".join(current_progress))
    print("Misses: %s" % ", ".join(wrong_guesses))

    remain_tries = word_length - loose_count
    print("Remaining tries: %d/%d" % (remain_tries, word_length))

def check_state():
    global win_count
    global loose_count

    if win_state(win_count) or loose_state(loose_count):
        restart()
    else:
        print_current_progress()
        input_guess_option()

def win_state(win_count):
    if win_count == word_length:
        print("Current progress: %s" % "".join(current_progress))
        print("Congratulations! You have guessed the word '%s'!" % word)
        return True
    else:
        return False

def loose_state(loose_count):
    if loose_count == word_length:
        hangman_pic.render_pic(loose_count, word_length)
        print("You have failed to guess the word '%s'. Good luck next time!" % word)
        return True
    else:
        return False

read_words()
menu()