import random

class PasswordGenerator:

    lower_case = ['a','b','c','d','e','f','g','h','i',
                'j','k','l','m','n','o','p','q','r',
                's','t','u','v','w','x','y','z']

    upper_case = [letter.upper() for letter in lower_case]

    numbers = ['0','1','2','3','4','5','6','7','8','9']

    special_chars = ['!','"','#','¤','%','&','/','(',')','=',
                    '?','"','@','£','$','{','[',']','}','\\']

    @classmethod
    def generate_password_character(cls, lenght: int):
        password_character_combo = [cls.lower_case, cls.upper_case, cls.numbers, cls.special_chars]
        for _ in range(lenght):
            # trunk-ignore(bandit/B311)
            yield random.choice(random.choice(password_character_combo))

if __name__ == '__main__':
    generator = PasswordGenerator()
    password = ''.join([c for c in PasswordGenerator.generate_password_character(8)])
    print(password)