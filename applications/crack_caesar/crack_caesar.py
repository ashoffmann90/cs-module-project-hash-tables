# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here


with open('./applications/crack_caesar/ciphertext.txt') as f:
    content = f.read()

# print(content)


def count_letters(s):
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count


print(count_letters(content))

# ## Challenge

# Write a program that automatically finds the key for the ciphertext in
# the file [`ciphertext.txt`](ciphertext.txt), then decodes it and shows
# the plaintext.

# (All non-letters should pass through the decoding as-is, i.e. spaces and
# punctuation should be preserved. The input will not contain any
# lowercase letters.)

# No tests are provided for this one, but the result should be readable,
# with at most a handful of incorrect letters.
