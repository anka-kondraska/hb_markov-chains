from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    one_long_source_string = open(file_path).read()
    return one_long_source_string

    

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    split_into_lots_of_tiny_strings = text_string.split()

    chains = {}

    #key is a bi-gram tuple, value is a list of strings which can follow the tuple

    # for index, word in enumerate(split_into_lots_of_tiny_strings):
    #     print index, word

    #     while index < len(split_into_lots_of_tiny_strings):

    for index in range(len(split_into_lots_of_tiny_strings)-1):
        key = (split_into_lots_of_tiny_strings[index], 
               split_into_lots_of_tiny_strings[index + 1])
        
        second_gram = key[1]
        print second_gram

        value = []
        
        # find all instances of second_gram and store the words that follow in a list
        for index, word in enumerate(split_into_lots_of_tiny_strings):
            
            if word == split_into_lots_of_tiny_strings[-2]:
                break

            # For all instances of second_gram, store the following word in value
            elif word == second_gram:   
                value.append(split_into_lots_of_tiny_strings[index + 2])

            chains[key] = value

        
    print chains  





def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
print input_text

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
