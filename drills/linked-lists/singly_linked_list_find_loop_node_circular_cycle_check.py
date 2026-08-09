# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None



# time O(n) - thats how many nodes SLOW will eventually travel
# space O(1)
def findLoop(head):
    # Write your code here.

    slow = head.next
    fast = head.next.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast

'''
                    X         Y
|---- D distance ---|----P----|
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
                    ^         v
                    9 <- 8 <- 7      
                    
slow travels: D + P
fast travels: 2D + 2P so double or "D + P + R + P"
distance from Y to X is: R
R = 2D + 2P - D - 2P = D (DRAW THIS AS IT REALLY HELPS)
Since distance where they meet is same as distance between head and X, then put fast node to head, make it travel 
    same as slow. They will  then meet at X. 
 
'''