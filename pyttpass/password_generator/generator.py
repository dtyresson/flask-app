import random
from english_words import get_english_words_set

class Generator:
    def generate():
        pass

class PassphraseGenerator(Generator):

    @classmethod
    def randomize_word_capitalization(cls, word_count: int):
        words =[]
        dictionary = get_english_words_set(['web2'], lower=True)
        for _ in range(word_count):
            word = random.choice(list(dictionary))
            words.append(''.join(
                random.choice(
                    random.choices((str.upper, str.lower), 
                                   weights=(10,50), 
                                   k=5)
                    )(char) for char in word
                ))
        return words

    @classmethod
    def generate(cls, word_count: int):
        return ''.join(cls.randomize_word_capitalization(word_count))

class PasswordGenerator(Generator):

    lower_case = ['a','b','c','d','e','f','g','h','i',
                  'j','k','l','m','n','o','p','q','r',
                  's','t','u','v','w','x','y','z']

    upper_case = [letter.upper() for letter in lower_case]

    numbers = ['0','1','2','3','4','5','6','7','8','9']

    special_chars = ['!','"','#','¤','%','&','/','(',')','=',
                     '?','|','@','£','$','{','[',']','}','\\']

    @classmethod
    def generate_password_characters(cls, lenght: int):
        generator_character_list = [cls.lower_case, cls.upper_case, cls.numbers, cls.special_chars]
        adjusted_probability = random.choices(generator_character_list, weights=(50,50,30,20), k=8)
        for _ in range(lenght):
            yield random.choice(random.choice(adjusted_probability))

    @classmethod
    def generate(cls, lenght: int):
        return ''.join([c for c in cls.generate_password_characters(lenght)])

if __name__ == '__main__':

    #password = PasswordGenerator.generate(12)
    password = PassphraseGenerator.generate(3)
    print(password)