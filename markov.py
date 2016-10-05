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

    split_string = text_string.split()
    # first_source_words = tuple(split_string[0:2])

    chains = {}

    # key is a bi-gram tuple, value is a list of strings which can follow the tuple
    for index in range(len(split_string)-2):

        key = (split_string[index], 
               split_string[index + 1])

        value = split_string[index +2]

        chains[key] = chains.get(key, [])
        chains[key].append(value)

    return chains





def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    tuple_seed = choice(chains.keys())

    #Pick a tuple seed
    while tuple_seed[0][0].isupper() == False: 
        tuple_seed = choice(chains.keys())

        
    
    text = ' '.join(tuple_seed)
   

    #loop
    while tuple_seed[1][-1] not in ".!?":

        value_options = chains.get(tuple_seed)
        value_choice = choice(value_options)
        text += " " + value_choice
        tuple_seed = (text.split()[-2], text.split()[-1])
    
    return text


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
