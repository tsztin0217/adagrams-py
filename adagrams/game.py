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

SCORE_DICT = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
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
    letters_available = letter_bank.copy()

    for letter in word.upper():
        if letter in letters_available:
            letters_available.remove(letter)
        else:
            return False
    return True



def score_word(word):
    total = 0

    if len(word) in [7, 8, 9, 10]:
        total += 8

    for letter in word.upper():
        for score, letters in SCORE_DICT.items():
            if letter in letters:
                total += score
    return total
            
    

def get_highest_word_score(word_list):
    scores_dict = {}
    highest_score = 0
    highest_word = ""

    for word in word_list:
        scores_dict[word] = score_word(word) # first fill in the empty dict with all words from list
        for scored_word, score in scores_dict.items(): # then loop through the filled dictionary
            if score > highest_score:
                highest_score = score # every time we get a higher score we replace the highest_score with current score
                highest_word = scored_word
            elif score == highest_score: # tie-breaking logic
                # if tied in both length and score:
                if score == highest_score and len(scored_word) == len(highest_word):
                    if len(highest_word) == 10: # since highest_word in before current word, we choose highest_word because it appears earlier
                        return(highest_word, highest_score) # stops here since 10 letters take priority
                # if there's a ten-letter word
                elif len(scored_word) == 10:
                    highest_word = scored_word
                    highest_score = score
                    return(highest_word, highest_score)
                elif len(scored_word) < len(highest_word):
                    highest_word = scored_word
                    highest_score = score
    return (highest_word, highest_score)
        