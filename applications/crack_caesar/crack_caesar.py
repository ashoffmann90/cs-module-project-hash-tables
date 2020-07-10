# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here


# standup code
cipher = open('./applications/crack_caesar/ciphertext.txt').read()


def create_key(s):
    count = {}
    order = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W',
             'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    # ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', "\\", '|', '[', ']', '{', '}','(',')','*','^','&',' ']
    # for i in ignore:
    # s=s.replace(i,'') #can use isalpha instead
    # count the letters
    for letter in s:
        # can add this instead of the s.replace
        if letter.isalpha():
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
    count = {key: value for key, value in sorted(
        count.items(), key=lambda item: item[1], reverse=True)}
    # print(count)
    for index, key in enumerate(count):
        if index >= len(order):
            continue
        count[key] = order[index]
    return count


def decode(s, key):
    r = ""
    for c in s:
        if c not in key:
            r += str(c)
        else:
            r += str(key[c])
    return r


key = create_key(cipher)
# print(key)
print(decode(cipher, key))


# william's code
# import string
# # Use frequency analysis to find the key to ciphertext.txt, and then
# # decode it.
# # import the message
# txt = open('./applications/crack_caesar/ciphertext.txt').read()
# cipher_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
#                'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
# cipher = {i: cipher_list[i] for i in range(0, len(cipher_list))}
# dictionary = {}
# alphabet = string.ascii_uppercase
# for character in txt:
#     for alpha in alphabet:
#         # if character.isalpha(): --> doesn't work for this scenario
#         if character in alpha and character not in dictionary:
#             # dictionary[character] = 1 if character not in dictionary else dictionary[character] + 1
#             dictionary[character] = 1
#     else:
#         if character in dictionary:
#             dictionary[character] += 1
# # sort d by highest freq to lowest
# sorted_dict = dict(
#     sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
# # loop through sorted_dict and replace all values with corresponding letter from cipher
# for index, key in enumerate(sorted_dict):
#     if index in cipher:
#         sorted_dict[key] = cipher[index]
# code = ''
# for i in txt:
#     if i in alphabet:
#         # print(i)
#         code += sorted_dict[i]
#     else:
#         code += i
# print(code)


# my crap code
# with open('./applications/crack_caesar/ciphertext.txt') as f:
#     content = f.read()

# # print(content)
# cipher = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
#           'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


# def count_letters(s):
#     count = {}
#     for c in s:
#         if c.isalpha():
#             count[c] = 1 if c not in count else count[c] + 1
#             # if c not in count:
#             #     count[c] = 1
#             # else:
#             #     count[c] += 1
#     return count


# x = count_letters(content)
# # print(x)

# item = {key: value for key, value in sorted(
#     x.items(), key=lambda e: e[1], reverse=True)}
# sorted = []

# # for i in item:
# #     sorted.append(i)
# #     print(f'{i[0]}: {i[1]}')
# # # print(sorted)


# for letter, value in item.items():
#     # print(value)
#     for cipher_letter in cipher:
#         item[value] = cipher_letter
# print(item)


# ## Challenge

# Write a program that automatically finds the key for the ciphertext in
# the file [`ciphertext.txt`](ciphertext.txt), then decodes it and shows
# the plaintext.

# (All non-letters should pass through the decoding as-is, i.e. spaces and
# punctuation should be preserved. The input will not contain any
# lowercase letters.)

# No tests are provided for this one, but the result should be readable,
# with at most a handful of incorrect letters.
