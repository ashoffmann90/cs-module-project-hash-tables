"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


# Your code here
sums = {}

diffs = {}

# iterate through q for every pair
for i in q:
    for j in q:
        # calculate sum
        s = f(i) + f(j)
        # store the pair that makes the sum
        if s in sums:
            sums[s].append((i, j))
        else:
            sums[s] = [(i, j)]

        # do same for diffs
        d = f(i) - f(j)
        if d in diffs:
            diffs[d].append((i, j))
        else:
            diffs[d] = [(i, j)]
# iterate through one, to check if the answer is in the other
for result in sums:
    if result in diffs:
        # print all combos of numbers that make the sum and diff
        for s in sums[result]:
            for d in diffs[result]:
                a, b, c, d = s[0], s[1], d[0], d[1]
                print(f'f({a}) + f({b}) = f({c}) - f({d})')


# run through f()
# add to left

# loop through for the left
# add to left dict

# loop through for the right
# add to right dict

answer = []
