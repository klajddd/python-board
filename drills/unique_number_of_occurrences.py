arr = [1, 2, 2, 2, 1, 1, 3]

occurrences = {}

for i in arr:
    if i in occurrences:
        occurrences[i] += 1
    else:
        occurrences[i] = 1

list_of_values = list(occurrences.values())

print(len(list_of_values) == len(set(list_of_values)))

# thisdict = {'make': 'ford', 'year': 1992}

# di = {}

# print(thisdict.items())
