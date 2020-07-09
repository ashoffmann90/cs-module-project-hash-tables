# Your code here

with open('applications/histo/robin.txt') as f:
    content = f.read()
# print(content)


count = {}
ignore_chars = ':,;.-+=/\\|[]{}()*^&"'


def histo(s):
    words = s.translate(str.maketrans(
        '', '', ignore_chars)).lower().split()
    # words = s.lower().split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


# print(histo(content))
count = histo(content)
count = sorted(count.items(), key=lambda x: (-x[1], x[0]))

# print(count)
width = max([len(word[0]) for word in count]) + 2

for num in count:
    print(f'{num[0].ljust(width)}' + '#' * num[1])

# Print a histogram showing the word count for each word, one hash mark
# for every occurrence of the word.

# Output will be first ordered by the number of words, then by the word
# (alphabetically).

# The hash marks should be left justified two spaces after the longest
# word.

# Case should be ignored, and all output forced to lowercase.

# Split the strings into words on any whitespace.

# Ignore each of the following characters:

# ```
# " : ; , . - + = / \ | [ ] { } ( ) * ^ &
# ```

# If the input contains no ignored characters, print nothing.

# items: `.items()` method on a dictionary might be useful.

# sorting: it's possible for `.sort()` to sort on multiple keys at once.

# sorting: negatives might help where `reverse` won't.

# printing: you can print a variable field width in an f-string with
# nested braces, like so `{x:{y}}`
