import random

#make a list of words
words = [
    'shihtzu',
    'poodle',
    'cute',
    'puppies',
    'fluffy',
    'love',
    'brats',
    'babies'
    ]

while True:
    start = input('Press enter/retrun to start, or enter Q to quit')
    if start.lower() == 'q':
        break
    
    #pick random word
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []
    
    while len(bad_guesse) < 7 and len(good_guesses) != len(list(secret_word)):
        #draw spaces
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end =' ')
            else:
                print(' ', end =' ')
    #take guess
    #draw guessed letters and strikes
    #print out win/lose
