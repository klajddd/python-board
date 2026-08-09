# time O(n)
# space O(n)
def sunsetViews(buildings, direction):
    # Write your code here.
    buildingsWithSunsetViews = []

    startIdx = 0  if direction == 'WEST' else len(buildings) - 1
    step = 1 if direction == 'WEST' else -1

    idx = startIdx
    runningMaxHeight = 0

    while idx >= 0 and idx < len(buildings):
        buildingHeight = buildings[idx]

        if buildingHeight > runningMaxHeight:
            buildingsWithSunsetViews.append(idx)

        runningMaxHeight = max(runningMaxHeight, buildingHeight)

        idx += step

    if direction == 'EAST':
        return buildingsWithSunsetViews[::-1]

    return buildingsWithSunsetViews
