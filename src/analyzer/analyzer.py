import sys
import os
from warnings import catch_warnings
from textx import metamodel_from_file
from os.path import join, dirname, exists
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from model.match import Match
from model.point import Point
from model.set import Set
from interpreter.interpreter import create_model, interpreter

def get_points_by_set(set, team):
    if team == 'A':
        return set.team_a_points()
    else:
        return set.team_b_points()

def longest_rally_for_set(set):
    rally_duration = 0
    for point in set.points:
        temp = point.num_of_assists()
        if temp > rally_duration:
            rally_duration = temp
    return rally_duration

def average_rally_for_set(set):
    sum = 0
    for point in set.points:
        sum += point.num_of_assists()
        
    return sum/len(set.points)

def serve_to_zone_by_set(set, team):
    #       1  2  3  4  5  6  zona
    zone = [0, 0, 0, 0, 0, 0]
    for point in set.points:
        if point.team == team:
            try:
                to_zone = int(point.serve.to_zone)
                zone[to_zone - 1] = zone[to_zone - 1] + 1
            except:
                continue

    return zone

def attack_to_zone_by_set(set, team):
    #       1  2  3  4  5  6  zona
    zone = [0, 0, 0, 0, 0, 0]
    # TO DO

    return zone

if __name__ == '__main__':
    file_name = join('..', sys.argv[1])
    model = interpreter(file_name)
    match = create_model(model)
   # print(get_points_by_set(match.sets[0], 'A'), 'TEAM A')
   # print(longest_rally_for_set(match.sets[0]), ' longest rally')
   # print(average_rally_for_set(match.sets[0]), ' average rallys')
    for z in serve_to_zone_by_set(match.sets[0], 'A'):
        print(z)
    