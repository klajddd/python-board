# time O(n) where n is length of shorter string
# space O(1)
def oneEdit(stringOne, stringTwo):
    # Write your code here.
    lengthOne, lengthTwo = len(stringOne), len(stringTwo)
    if abs(lengthOne - lengthTwo) > 1:
        return False
    madeEdit = False
    indexOne = 0
    indexTwo = 0

    while indexOne < lengthOne and indexTwo < lengthTwo:
        if stringOne[indexOne] != stringTwo[indexTwo]:
            if madeEdit:
                return False
            madeEdit = True

            if lengthOne > lengthTwo:
                indexOne += 1
            elif lengthTwo > lengthOne:
                indexTwo += 1
            else:
                indexOne += 1
                indexTwo += 1
        else:
            indexOne += 1
            indexTwo += 1

    return True

# ======================================================================================================================


# time O(n+m) where n length of stringOne, m length of stringTwo
# space O(n+m)
def oneEdit(stringOne, stringTwo):
    # Write your code here.
    lengthOne, lengthTwo = len(stringOne), len(stringTwo)
    if abs(lengthOne - lengthTwo) > 1:
        return False

    for i in range(min(lengthOne, lengthTwo)):
        if stringOne[i] != stringTwo[i]:
            if lengthOne > lengthTwo:
                return stringOne[i + 1 :] == stringTwo[i:]
            elif lengthTwo > lengthOne:
                return stringOne[i:] == stringTwo[i + 1 :]
            else:
                return stringOne[i + 1 :] == stringTwo[i + 1 :]
    return True