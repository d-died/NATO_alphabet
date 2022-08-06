student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)
#
import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
#     print(row.score)
#     if row.student == "Angela":
#         print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
n_a_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(n_a_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_to_translate = input("Choose a word: ").upper()
split_word = [letter for letter in word_to_translate]
letters_list = [n_a_dict[letter] for letter in split_word]
