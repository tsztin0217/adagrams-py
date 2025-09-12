from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

# create helper function to create a list of all available letters to use
def create_letter_list():
    letters = ""

    for letter, quantity in LETTER_POOL.items():
        if quantity > 0:
            letters += (letter * quantity)

    letter_list = list(letters)
    return letter_list

def draw_letters():
    letter_list = create_letter_list()
    hand = []
    while len(hand) < 10:
        random_index = randint(0, len(letter_list) - 1)
        hand.append(letter_list[random_index])
        letter_list.pop(random_index)
    return hand



def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass