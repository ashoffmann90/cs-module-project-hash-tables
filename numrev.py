cache = {}

"""
def build_lookup_table():
    for i in range(1000):
	cache[i] = num_reverse(i)
"""


def num_reverse(n):
    if n in cache:
        return cache[n]

    n2 = list(str(n))
    n2.reverse()
    n2 = ''.join(n2)

    cache[n] = int(n2)

    return cache[n]

# build_lookup_table()


print(num_reverse(123))
print(num_reverse(123))
print(num_reverse(123))
print(num_reverse(123))
print(num_reverse(123))
print(num_reverse(123))
print(num_reverse(123))
print(num_reverse(123))
