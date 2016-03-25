#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the
# command line with two arguments: the name of a file containing text to read, and the number of words
# to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game
# went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the
# Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit.
# Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started
# learning about what you're trying to make.

import sys
import random
import string


def build_markov_dict(filename):
    d = {}
    f = open(filename)
    for line in f:
        line = line.translate(string.maketrans("",""),string.punctuation).split()
        if len(line) < 3: continue
        for i in range(len(line)-3):
            tupkey = (line[i], line[i+1])
            try:
                d[tupkey].append(line[i+2])
            except KeyError:
                d[tupkey] = list()
                d[tupkey].append(line[i+2])
    return d


def generate_markov_text(d, words):
    prefix = random.choice(list(d.keys()))
    result = prefix[0] + " " + prefix[1] + " "
    while len(result.split()) < words:
        try:
            d[prefix]
        except KeyError:
            prefix = random.choice(list(d.keys()))
            result += prefix[0] + " " + prefix[1] + " "
        word = random.choice(d[prefix])
        result += word + " "
        prefix = new_prefix(prefix, word)
    print(result)


def new_prefix(prefix, word):
    return (prefix[1], word)


def main(argv):
    markov = build_markov_dict(argv[1])
    generate_markov_text(markov, argv[2])


if __name__ == '__main__':
    try:
        sys.argv[2] = int(sys.argv[2])
    except IndexError:
        print('Usage: markov.py <input file> <# words to generate>')
        sys.exit(1)
    main(sys.argv)
