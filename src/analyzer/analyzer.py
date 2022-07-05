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
    for p in set.points:
        for assist in p.assists:
            for a in assist.actions:
                if a.player.team == team:
                    try:
                        to_zone = int(a.to_zone)
                        zone[to_zone - 1] = zone[to_zone - 1] + 1
                    except:
                        continue
    
    return zone

def attack_to_zone_by_set_percent(set, team):
    #               1  2  3  4  5  6  zona
    zone_percent = [0, 0, 0, 0, 0, 0]
    zone = attack_to_zone_by_set(set, team)
    sum = 0
    for z in zone:
        sum += z
    for i in range(len(zone)):
        zone_percent[i] = round(100*zone[i]/sum, 1)
    return zone_percent

def serve_err_by_set(set, team):
    count = 0
    for p in set.points:
        if p.team == team:
            try:
                end_of_point = p.serve.end_of_point
                if end_of_point == 'out' or end_of_point == 'net':
                    count += 1
            except:
                continue
    return count

def serve_ace_by_set(set, team):
    count = 0
    for p in set.points:
        if p.team == team:
            try:
                end_of_point = p.serve.end_of_point
                if end_of_point == 'ace':
                    count += 1
            except:
                continue
    return count

def team_wins_set(set):
    team_a_points = get_points_by_set(set, 'A')
    team_b_points = get_points_by_set(set, 'B')
    if team_a_points > team_b_points:
        return 'A'
    else:
        return 'B'

def reception_err_by_set(set, team):

    pass

if __name__ == '__main__':
    file_name = join('..', sys.argv[1])
    model = interpreter(file_name)
    match = create_model(model)
   # print(get_points_by_set(match.sets[0], 'A'), 'TEAM A')
   # print(longest_rally_for_set(match.sets[0]), ' longest rally')
   # print(average_rally_for_set(match.sets[0]), ' average rallys')
   # for z in attack_to_zone_by_set_percent(match.sets[0], 'A'):
   #     print(z)
    