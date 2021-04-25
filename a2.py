
# updated dictionary with 53 words and with a new domain of hanging out with family
# (watching a movie and singing and going for a drive)
EtoF = {'with' : 'avec', 'I' : 'je', 'watch' : 'regarde', 'movie' : 'film', 'family' : 'famille',
        'sings' : 'chante', 'happy' : 'heureux', 'and' : 'et', 'of' : 'du', 'members' : 'membres',
        'the' : 'le', 'is' : 'est', 'very' : 'très', 'sad' : 'triste', 'beautiful' : 'beau',
        'like' : 'aime', 'it' : 'ceci', 'but' : 'mais', 'not' : 'pas', 'my' : 'mon',
        'if' : 'si', 'they' : 'ils', 'we' : 'nous', 'eat' : 'mange',
        'popcorn' : 'popcorn', 'also' : 'aussi', 'juice' : 'jus', 'make' : 'crée',
        'plans' : 'plans', 'go' : 'allons', 'for' : 'pour', 'a': 'un', 'drive' : 'conduit',
        'Therefore' : 'donc', 'almost' : 'presque', 'hit' : 'frappe' , 'cat' : 'chat',
        'start' : 'commence', 'radio' : 'radio', 'our' : 'notre', 'favorite' : 'favori',
        'music' : 'musique', 'plays' : 'joue', 'reminisce' : 'souvient', 'all' : 'tous',
        'memories' : 'memoires', 'have' : 'avons', 'from' : 'de', 'sing' : 'chante',
        'many' : 'beaucoup', 'me' : 'moi', 'brother' : 'frère', 'drink' : 'bois'}

dct = {}
# function that reverses EtoF dict to FtoE to use it when needed
def reverseDictionary(dictionary):
    for k, v in dictionary.items():
        dct[v] = k
    return dct
FtoE = reverseDictionary(EtoF)

dicts = {'English to French': EtoF, 'French to English': FtoE}

# function that returns the translated word of a certain word
def translateWord(word, dictionary) :
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word

def translate(phrase, dicts, direction) :
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters
    dictionary = dicts[direction]
    translation = ''
    word = ''

    # this part of the program takes the first letter of the sentence
    # which is a capital letter and turns it into lower case before
    # going through the dictionary
    phrase = list(phrase.split())
    lower = []
    if phrase[0] != 'I':
        for m in phrase[0]:
            lower.append(m)
        lower[0] = lower[0].lower()
        lower = ''.join(lower)
        phrase[0] = lower
        phrase = ' '.join(phrase)
    else:
        phrase = ' '.join(phrase)

    # this part goes through every word in the sentence and get the translated sentence
    for character in phrase :
        if character in letters :
            word = word + character
        else :
            translation = translation + translateWord(word, dictionary) + character
            word = ''
    translation = translation + translateWord(word, dictionary) + character

    # this part takes out the extra period at the end of the translated sentence
    translation = list(translation)
    translation.pop()
    translation = ''.join(translation)
    # this part changes the first letter of the sentence into capital letter
    translation = list(translation.split())
    if len(translation) > 1:
        upper = []
        for i in translation[0]:
            upper.append(i)
        upper[0] = (upper[0]).upper()
        upper = ''.join(upper)
        translation[0] = upper
    translation = ' '.join(translation)
    return translation

# function that asks the user if they want to translate from E to F or from F to E
# it asks the user until they put in the right input
def whatToTrans(trans):
    language = ''
    while language == 'E to F' or 'F to E':
        language = input('Please enter one of the following: (E to F/F to E): \n')
        if language == 'E to F':
            language = 'English to French'
            break
        elif language == 'F to E':
            language = 'French to English'
            break
        else:
            print("Sorry I don't understand")
    return translate(trans, dicts, language)

# Function for adding new words and their definitions into the dictionary before using the translator.
# You can stop adding words by entering '/' and it will return the updated dictionary.
# After that, it'll call whatToTrans() function to translate user's input, until the user enters '/'.
def addToDict():
    word = ''
    while word != '/':
        word = input('Enter the word you want to add (enter / to stop): \n')
        if word in EtoF:
            print('That word is already in the dictionary.')
        elif word == '/':
            break
        else:
            definition = input('Enter its definition: \n')
            EtoF[word] = definition
    print("Here's your updated dictionary.")
    print(EtoF)
    print('--------------------------------------')
    trans = ''
    while trans != '/':
        trans = input('What do you want to translate? (enter / to stop) \n')
        if trans == '/':
            break
        print(whatToTrans(trans))
    print('--------------------------------------')
    return EtoF


if __name__ == "__main__":

    # these are samples of already translated sentences using the new domain
    print('Samples:')
    print('--------------------------------------')
    sentences_EtoF = ['I watch a movie with my family members.', 'The movie is very sad but beautiful.',
                      'I like it but not my brother.', 'We eat popcorn and drink juice.', 'We go for a drive.']
    # a for loop to translate a list of english sentences
    for i in sentences_EtoF:
        translated = translate(i, dicts, 'English to French')
        print('Input:', i)
        print('Output:', translated)
        print('--------------------------------------')

    lst_sentences_FtoE = ['Je commence le radio.', 'Notre favori musique joue.', 'Si je chante ils chante avec moi.',
                          'Je souvient tous le memoires.', 'Nous presque frappe un chat.']
    # a for loop to translate a list of french sentences
    for j in lst_sentences_FtoE:
        translated = translate(j, dicts, 'French to English')
        print('Input:', j)
        print('Output:', translated)
        print('--------------------------------------')

    # This part asks the user if they want to add any new words to the dictionary before using the translator.
    # If the user answers yes, it calls addToDict() function and if the user answers no,
    # it asks what to translate and calls whatToTrans() function until the user enters '/'.
    hello = input(
        '''Hello there,
would you like add a word to the dictionary
before using the translator? (answer using :y/n) \n''')
    if hello == 'y':
        addToDict()
    elif hello == 'n':
        trans = ''
        while trans != '/':
            trans = input('What do you want to translate? (enter / to stop) \n')
            if trans == '/':
                break
            print(whatToTrans(trans))
        print('--------------------------------------')