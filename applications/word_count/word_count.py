counts = {}


def word_count(s):
    # Your code here
    # check for special chars, remove
    # convert string to lowercase
    # for each letter in array
    ignored_chars = {'"': None, ':': None, ';': None, ',': None, '.': None, '-': None, '+': None, '=': None, '/': None,
                     '\\': None, '|': None, '[': None, ']': None, '{': None, '}': None, '(': None, ')': None, '*': None, '^': None, '&': None, }
    for char in s:
        # if letter is in dict of ignored chars
        if char in ignored_chars:
            # remove that from the array
            s.replace(char, '')

    # count each word, return count of each word
    # str.split()
    words = s.lower().split(' ')

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
