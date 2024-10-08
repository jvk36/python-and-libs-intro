import pandas


df = pandas.read_csv("./data/nato_phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(alpha_dict)


def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        phonetic_codes = [alpha_dict[letter] for letter in user_word]  # if letter.isalpha()]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_codes)


generate_phonetic()
