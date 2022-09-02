def tournamentWinner(competitions, results):
    best_team = ""
    scores = {best_team: 0}

    for index, competition in enumerate(competitions):
        result = results[index]
        home_team, away_team = competition
        winning_team = home_team if result == 1 else away_team

        update_score(winning_team, 3, scores)
        if scores[winning_team] > scores[best_team]:
            best_team = winning_team
    return best_team


def update_score(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points