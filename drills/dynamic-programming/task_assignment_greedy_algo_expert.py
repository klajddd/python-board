# time O(n log n)
# space O(n)
def taskAssignment(k, tasks):
    # Write your code here.
    result = []
    tasksIndexes = []
    for i in range(2 * k):
        tasksIndexes.append(i)
    tasks = list(zip(tasks, tasksIndexes))
    tasks.sort(key=lambda x: x[0])

    for i in range((2 * k) // 2):
        worker = []
        worker.append(tasks[i][1])
        worker.append(tasks[2 * k - 1 - i][1])
        result.append(worker)
    return result
