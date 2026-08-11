# time O(n log n)
# space O(1)

def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    # red or blue
    # sort them
    redShirtHeights.sort()
    blueShirtHeights.sort()

    print(redShirtHeights)
    print(blueShirtHeights)

    redsFront = None

    if redShirtHeights[0] < blueShirtHeights[0]:
        redsFront = True
    elif redShirtHeights[0] > blueShirtHeights[0]:
        redsFront = False
    else:
        return False

    for i in range(1, len(redShirtHeights)):
        if redsFront:
            if redShirtHeights[i] < blueShirtHeights[i]:
                continue
            else:
                return False
        else:
            if redShirtHeights[i] > blueShirtHeights[i]:
                continue
            else:
                return False

    return True


'''
{
  "blueShirtHeights": [6, 9, 2, 4, 5],
  "redShirtHeights": [5, 8, 1, 3, 4]
}
result = True
'''