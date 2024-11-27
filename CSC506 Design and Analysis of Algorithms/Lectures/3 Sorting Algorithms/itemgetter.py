import operator

teams = []
teams.append(('Lightning', 45, 17, 94))
teams.append(('Capitals', 37, 21, 81))
teams.append(('Predators', 42, 14, 93))
teams.append(('Golden Knights', 41, 18, 87))

results = sorted(teams, key = operator.itemgetter(0))
print('%15s%4s%4s%4s' % ("Team", "W", "L", "Pts"))

for team in results:
    print('%15s%4d%4d%4d' % team)
