"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    global content
    content = open(file_path).read().split()
    return content
# open_and_read_file("green-eggs.txt")


def make_chains(content):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    global chains
    chains = {}
    for index in range(len(content) - 2):
        bigram = (content[index], content[index + 1])
        transitions = content[index + 2]
        if bigram not in chains:
            chains[bigram] = [transitions]
        else:
            chains[bigram].append(transitions)

    
    # your code goes here
    # print(chains)
    return chains
# make_chains(content)

def make_text(chains):
    """Return text from chains."""

    words = []
    keys_list = list(chains.keys()) # makes a list of our bigrams as tuples
    # print(keys_list)
    random_bigram = choice(keys_list) # picks a random bigram from our list and names it
    # print(random_bigram)
    
    words.extend(random_bigram)

  
    while random_bigram in chains: # While there are places to go from my current state
        random_transition = choice(chains[random_bigram]) # picks a random value from our key (random_bigram)
        # print(random_transition)
        words.append(random_transition)
        # bigram = ("Sam", "I")
        # transition = "am?"

        random_bigram = (random_bigram[1], random_transition)
        #print(words)
        # for key in keys_list:
        #     if random_transition == key[0]:
        #         words.append(key)

    # print(words)


        # if chains[] = random_transition:
    # your code goes here

    return ' '.join(words)



input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

