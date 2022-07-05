import sys
import os
from textx import metamodel_from_file
from os.path import join, dirname, exists
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from model.match import Match
from model.point import Point
from model.set import Set

def interpreter(file_name):
    meta_model = metamodel_from_file('..\\grammar\\grammar.tx')
    model = meta_model.model_from_file(file_name)
    return model

def create_model(model):
    points = []
    match = Match(model.sets, model.team_a, model.team_b)
    for j in range(len(model.sets)):
        set = Set(match.sets[j].set_num, [])
        for i in range(len(match.sets[j].points)):
            set.points.append(Point(match.sets[j].points[i].team, match.sets[j].points[i].serve, match.sets[j].points[i].assists))
        match.sets[j] = set
    return match



    