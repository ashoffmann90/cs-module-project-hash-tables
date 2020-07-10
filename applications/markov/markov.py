import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words = words.split()
# print(words)

following = {}

prev = None

# loop through
for word in words:
    if prev is not None:
        if prev not in following:
            following[prev] = []
        # add word to the list of those words that are following
        following[prev].append(word)
    prev = word

# words that we can start a sentence with
# if word[0] (first letter of the word) is uppercase OR the length of the word is greater than 1 AND word[1] (character 2) is uppercase
    # then add word to is_good_start


def is_good_start(x): return x[0].isupper() or len(x) > 1 and x[1].isupper()


# if word in following.keys() AND word in is_good_start
# then start_words = word
start_words = [w for w in following.keys() if is_good_start(w)]

# print number of paragraphs
for i in range(5):
    # choose the starting word at random from start_words
    word = random.choice(start_words)

    # initialize stopped to False
    stopped = False
    # initialize stop_punctuation
    # stops when it gets to any of these characters.
    stop_punctuation = '.!?\"'

    while not stopped:
        # print the word, and follow it with a space
        print(word, end=' ')

        # if the last character in a word is in stop_punctuation OR the len of the word is greater than 1 AND the second to last character is in stop_punc
        if word[-1] in stop_punctuation or len(word) > 1 and word[-2] in stop_punctuation:
            # then STOP
            stopped = True
        else:
            # otherwise continue to next word until it stop
            next_words = following[word]
            word = random.choice(next_words)

    print("\n")


# TODO: construct 5 random sentences
# Your code here


# 1. Read the file `input.txt` and split it into words.

#    Don't worry about changing punctuation or capitalization. For
#    example, a "word" might be `"Hello,`. Just leave it all in there.

# 2. Analyze the text, building up the dataset of which words can follow
#    particular words.

#    (Hint: leave duplicates in for this part. If a the word `and` is seen
#    following the word `goats` multiple times, include all those `and`s.
#    It'll give more convincing results because it is modelling the
#    _frequency_ of _how often_ a word follows another word.)

# 3. Choose a random "start word" to begin.

# 4. Loop through:

#    * Print the word.
#    * If it's a "stop word", stop.
#    * Else randomly choose a word that can follow this one.

# Start words are words that begin with a capital, or a `"` followed by a
# capital.

# Stop words are words that end in any of the punctuation `.?!`, or that
# punctuation followed by a `"`.

# Hints:

# * `random.choice()` can choose a random word out of a list.
# * `print(s, end=" ")` will print a space after every word instead of a
#   newline.

# There is no test file for this. Just see if it makes good nonsense.
