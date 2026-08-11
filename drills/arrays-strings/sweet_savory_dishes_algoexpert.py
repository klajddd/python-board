'''
have not studies this
'''

def sweetAndSavory(dishes, target):
    # Write your code here.
    sweetDishes = sorted([dish for dish in dishes if dish <0], key=abs)
    savoryDishes = sorted([dish for dish in dishes if dish > 0])

    bestPair = [0, 0]
    bestDifference = float('inf')
    sweetIndex, savoryIndex = 0, 0

    while sweetIndex < len(sweetDishes) and savoryIndex < len(savoryDishes):
        currentSum = sweetDishes[sweetIndex] + savoryDishes[savoryIndex]

        if currentSum <= target:
            currentDifference = target - currentSum
            if currentDifference < bestDifference:
                bestDifference = currentDifference
                bestPair = [sweetDishes[sweetIndex], savoryDishes[savoryIndex]]
            savoryIndex += 1
        else:
            sweetIndex += 1
    return bestPair
