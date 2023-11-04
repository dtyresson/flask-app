import random
from english_words import get_english_words_set

class CharTypes:

    LOWER = ('a','b','c','d','e','f','g','h','i',
                  'j','k','l','m','n','o','p','q','r',
                  's','t','u','v','w','x','y','z')

    UPPER = tuple(letter.upper() for letter in LOWER)

    NUMBER = ('0','1','2','3','4','5','6','7','8','9')

    SPECIAL = ('!','"','#','¤','%','&','/','(',')','=',
                     '?','|','@','£','$','{','[',']','}','\\')

class Generator:
    def generate():
        pass

class PassphraseGenerator(Generator):

    @classmethod
    def randomize_word_capitalization(cls, word_count: int):
        dictionary = get_english_words_set(['web2'], lower=True)
        for _ in range(word_count):
            word = random.choice(list(dictionary))
            yield ''.join(random.choice(random.choices((str.upper, str.lower), weights=(10,50), k=5))(char) for char in word)

    @classmethod
    def generate(cls, word_count: int):
        return ''.join(list(cls.randomize_word_capitalization(word_count)))

class PasswordGenerator(Generator):

    @classmethod
    def randomize_password_characters(cls, lenght: int, adjusted_char_probability):
        for _ in range(lenght):
            yield random.choice(random.choice(adjusted_char_probability))

    @classmethod
    def generate(cls, lenght: int, *args):

        #TODO Adjust dynamic weights
        adjusted_char_probability = random.choices(args, weights=(50,50,30,20), k=len(args)*2)
        return ''.join(list(cls.randomize_password_characters(lenght, adjusted_char_probability)))

if __name__ == '__main__':

    print(PasswordGenerator.generate(12, CharTypes.LOWER, CharTypes.UPPER, CharTypes.NUMBER, CharTypes.SPECIAL))
    print(PassphraseGenerator.generate(3))