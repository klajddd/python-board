# time O(n log n)
# space O(1)
# algo expert
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    total = 0
    if fastest:
        blueShirtSpeeds.sort(reverse=True)
        for i in range(len(redShirtSpeeds)):
            total += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    else:
        blueShirtSpeeds.sort()
        for i in range(len(redShirtSpeeds)):
            total += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return total

'''
place 1 blue shirt biker with 1 red shirt biker in same bike, speed of bike would be max of both bikers
if "fastest" if True, find max possible speed
if fastest is False, find min possible speed
 
{
  "blueShirtSpeeds": [3, 6, 7, 2, 1],
  "fastest": true,
  "redShirtSpeeds": [5, 5, 3, 9, 2]
}
res = 32
'''