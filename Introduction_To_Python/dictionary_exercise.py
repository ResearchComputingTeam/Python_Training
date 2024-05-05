from pprint import pprint

# Create an Arabic to English dictionary for the numbers 1 to 5
arabic_to_english = {} #optional

# Populate the dictionary
arabic_to_english = {"wahid": {"translation":"one", "is_even":False},
                      "ithnain":{"translation":"two", "is_even":True},
                      "thalatha":{"translation":"three", "is_even":False},
                      "arba3a":{"translation":"four", "is_even":True},
                      "khamsa":{"translation":"five", "is_even":False}}


# pprint(arabic_to_english["thalatha"]["translation"])

for entry in arabic_to_english:
    if arabic_to_english[entry]["is_even"] is False:
        pprint(arabic_to_english[entry]["translation"])

# pprint(arabic_to_english)


# Alternative with dico of list
# Populate the dictionary
arabic_to_english_dico_list = {"wahid": ["one", False],
                          "ithnain":["two", True],
                          "thalatha":["three", False],
                          "arba3a":["four", True],
                          "khamsa":["five", False]}

print(arabic_to_english_dico_list["arba3a"][1])

pprint(arabic_to_english_dico_list)

for element in arabic_to_english_dico_list:
    if arabic_to_english_dico_list[element][1] is False:
        pprint(arabic_to_english_dico_list[element][0])


new_list = list(arabic_to_english.items())

pprint(new_list)