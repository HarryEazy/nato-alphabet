import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}


def generate_phonetic_alphabet():

    user_word = input("Enter word: ").upper()
    try:
        code_list = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry only letter in the alphabet please")
        generate_phonetic_alphabet()
    else:
        print(code_list)



generate_phonetic_alphabet()
