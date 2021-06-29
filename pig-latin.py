vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]


def pig_latin(sentence):
    """
    This works with str_converter to convert a given sentence into pig latin
    :param sentence: taken from str_converter, user-inputted string
    :return: a newly converted string
    """

    new_list = []  # creates new list to store converted words

    for word in sentence:  # parses through the words in the given sentence using pig latin conditionals
        if word[0] not in vowels:
            new_word = word[1:] + word[0] + "ay"
            new_list.append(new_word)
        elif word[0] in vowels:
            new_word = word + "hay"
            new_list.append(new_word)

    for words in new_list:  # prints list as sentence for simple UI
        print(words, end=" ")

    print()


def str_converter():
    """
    Converts a user-inputted string for use in the pig_latin function
    """

    while True:
        print("Type 'QUIT' to end program")
        string = input("Enter a string with just words and spaces (no punctuation) ")
        if string == "QUIT":
            break
        else:
            lowercase_string = string.lower()  # makes string lowercase
            string_list = lowercase_string.split()  # splits string into individual words for list
            pig_latin(string_list)


str_converter()
