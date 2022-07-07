
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

def prepare_attacks_data(set, team):
    attacks_to_zone_by_set = attack_to_zone_by_set(set, team)
    attacks_to_zone_by_set_percent =attack_to_zone_by_set_percent(set, team)
    zone1 = str(attacks_to_zone_by_set[0]) + '  ['+ str(attacks_to_zone_by_set_percent[0])  + '%]'
    zone2 = str(attacks_to_zone_by_set[1]) + '  ['+ str(attacks_to_zone_by_set_percent[1])  + '%]'
    zone3 = str(attacks_to_zone_by_set[2]) + '  ['+ str(attacks_to_zone_by_set_percent[2])  + '%]'
    zone4 = str(attacks_to_zone_by_set[3]) + '  ['+ str(attacks_to_zone_by_set_percent[3])  + '%]'
    zone5 = str(attacks_to_zone_by_set[4]) + '  ['+ str(attacks_to_zone_by_set_percent[4])  + '%]'
    zone6 = str(attacks_to_zone_by_set[5]) + '  ['+ str(attacks_to_zone_by_set_percent[5])  + '%]'
    attacks = {
        'zone1': zone1,
        'zone2': zone2,
        'zone3': zone3,
        'zone4': zone4,
        'zone5': zone5,
        'zone6': zone6,
    }
    return attacks

def prepare_tabulate_attacks_data(match,team):
    if team == 'A':
        team_name = match.team_a
    else:
        team_name = match.team_b

    set1_attacks = prepare_attacks_data(match.sets[0], team)
    set2_attacks = prepare_attacks_data(match.sets[1], team)
    set3_attacks = prepare_attacks_data(match.sets[2], team)

    header_attack = ['Team '+ team_name , 'Set1', 'Set 2','Set 3']
    data_attack = [
    ['Attack to zone 1', set1_attacks['zone1'], set2_attacks['zone1'], set3_attacks['zone1']],
    ['Attack to zone 2', set1_attacks['zone2'], set2_attacks['zone2'], set3_attacks['zone2']],
    ['Attack to zone 3', set1_attacks['zone3'], set2_attacks['zone3'], set3_attacks['zone3']],
    ['Attack to zone 4', set1_attacks['zone4'], set2_attacks['zone4'], set3_attacks['zone4']],
    ['Attack to zone 5', set1_attacks['zone5'], set2_attacks['zone5'], set3_attacks['zone5']],
    ['Attack to zone 6', set1_attacks['zone6'], set2_attacks['zone6'], set3_attacks['zone6']]
]
    table_data = {
        'header':header_attack,
        'data':data_attack
    } 
    return table_data

