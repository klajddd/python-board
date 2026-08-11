# time O(n) - competitions
# space O(k) - teams
def tournamentWinner(competitions, results):
    # Write your code here.
    from collections import defaultdict

    winner = defaultdict(int)
    for i in range(len(competitions)):
        w = results[i]
        if w is 1:
            winner[competitions[i][0]] += 3
        else:
            winner[competitions[i][1]] += 3

    most = 0
    winnerTeam = None

    for team, score in winner.items():
        if score > most:
            winnerTeam = team
            most = score

    return winnerTeam


# ----------------------------------------------------------------------------------------------------------------------

competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]
  ]

results = [0, 1, 1]

print(tournamentWinner(competitions, results))