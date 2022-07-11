
from src.model.match import Match
from src.model.point import Point
from src.model.set import Set


def create_model(model):
    points = []
    match = Match(model.sets, model.team_a, model.team_b)
    for j in range(len(model.sets)):
        set = Set(match.sets[j].set_num, [])
        for i in range(len(match.sets[j].points)):
            set.points.append(Point(match.sets[j].points[i].team, match.sets[j].points[i].serve, match.sets[j].points[i].assists))
        match.sets[j] = set
    return match



    