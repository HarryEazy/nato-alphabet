import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

user_word = input(str("Enter word: ")).upper()
code_list = [nato_dict[letter] for letter in user_word if letter in nato_dict.keys()]

print(code_list)

