
from random import choice
import os
import discord

def open_and_read_file(file_path):
    """Take file path as string; return text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # your code goes here
    # 'Return contents of your file as one long string'

    path = str(file_path)
    get = open(path)
    doc = get.read()
    get.close()
    return doc



def make_chains(text_string):
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

    chains = {}

    # your code goes here

    words = text_string.split()
    words.append(None)


    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        val = words [i + 2]
        if key not in chains:
            chains[key] = []
        chains[key].append(val)
            
    return chains


def make_text(chains):
    """Return text from chains."""


    # your code goes here
    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    while word != None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

    return ' '.join(words)

# File input
input_path = 'green-eggs.txt'
# input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# For Testing purposes 
# print(chains) 

# Produce random text
random_text = make_text(chains)

print(random_text)


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(random_text)

client.run(os.environ['DISCORD_TOKEN'])

