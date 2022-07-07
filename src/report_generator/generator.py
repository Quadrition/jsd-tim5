
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from analyzer.analyzer import *


def prepare_set_data(set, team):
    points = get_points_by_set(set, team)
    serve_err = serve_err_by_set(set, team)
    serve_ace =  serve_ace_by_set(set, team)
    data = {
        'points': points,
        'serve_err': serve_err,
        'serve_ace': serve_ace
    }
    return data


def prepare_table_sets_data(match, team):
    if team == 'A':
        team_name = match.team_a
    else:
        team_name = match.team_b

    set1_data = prepare_set_data(match.sets[0], team)
    set2_data = prepare_set_data(match.sets[1], team)
    set3_data = prepare_set_data(match.sets[2], team)

    header = ['Team '+ team_name , 'points', 'serve error','serve ace']
    data = [
    ['Set 1', set1_data['points'], set1_data['serve_err'],set1_data['serve_ace']],
    ['Set 2', set2_data['points'], set2_data['serve_err'],set2_data['serve_ace']],
    ['Set 3', set3_data['points'], set3_data['serve_err'],set3_data['serve_ace']]
]
    table_data = {
        'header':header,
        'data':data
    } 
    return table_data
