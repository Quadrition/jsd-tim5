
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from analyzer.analyzer import *
import csv
from fpdf import FPDF


def prepare_set_data_per_team(set, team):
    points = get_points_by_set(set, team)
    serve_err = serve_err_by_set(set, team)
    serve_ace =  serve_ace_by_set(set, team)
    data = {
        'points': points,
        'serve_err': serve_err,
        'serve_ace': serve_ace
    }
    return data


def prepare_table_sets_data_per_team(match, team):
    if team == 'A':
        team_name = match.team_a
    else:
        team_name = match.team_b

    set1_data = prepare_set_data_per_team(match.sets[0], team)
    set2_data = prepare_set_data_per_team(match.sets[1], team)
    set3_data = prepare_set_data_per_team(match.sets[2], team)

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

def prepare_serve_data(set, team):
    serves_to_zone_by_set = serve_to_zone_by_set(set, team)
    zone1 = serves_to_zone_by_set[0] 
    zone2 = serves_to_zone_by_set[1] 
    zone3 = serves_to_zone_by_set[2] 
    zone4 = serves_to_zone_by_set[3] 
    zone5 = serves_to_zone_by_set[4] 
    zone6 = serves_to_zone_by_set[5] 
    serves = {
        'zone1': zone1,
        'zone2': zone2,
        'zone3': zone3,
        'zone4': zone4,
        'zone5': zone5,
        'zone6': zone6,
    }
    return serves

def prepare_tabulate_serve_data(match, team):
    if team == 'A':
        team_name = match.team_a
    else:
        team_name = match.team_b

    set1_serve = prepare_serve_data(match.sets[0], team)
    set2_serve = prepare_serve_data(match.sets[1], team)
    set3_serve = prepare_serve_data(match.sets[2], team)

    header_serve = ['Team '+ team_name , 'Set1', 'Set 2','Set 3']
    data_serve = [
    ['Serve to zone 1', set1_serve['zone1'], set2_serve['zone1'],set3_serve['zone1']],
    ['Serve to zone 2', set1_serve['zone2'], set2_serve['zone2'],set3_serve['zone2']],
    ['Serve to zone 3', set1_serve['zone3'], set2_serve['zone3'],set3_serve['zone3']],
    ['Serve to zone 4', set1_serve['zone4'], set2_serve['zone4'],set3_serve['zone4']],
    ['Serve to zone 5', set1_serve['zone5'], set2_serve['zone5'],set3_serve['zone5']],
    ['Serve to zone 6', set1_serve['zone6'], set2_serve['zone6'],set3_serve['zone6']]

]
    table_data = {
        'header':header_serve,
        'data':data_serve
    } 
    return table_data

def prepare_table_sets_data(match):
    header_sets = ['','longest rally','average rally']
    data_sets = [
        ['Set 1', longest_rally_for_set(match.sets[0]), average_rally_for_set(match.sets[0])], 
        ['Set 2', longest_rally_for_set(match.sets[1]), average_rally_for_set(match.sets[1])] ,
        ['Set 3', longest_rally_for_set(match.sets[2]), average_rally_for_set(match.sets[2])]
        ]
    sets_data = {
        'header_sets':header_sets,
        'data_sets':data_sets
    }
    return sets_data

def get_team_table_data(match, team):
    #Team table data per set 
    table_sets_data = prepare_table_sets_data_per_team(match, team)
    header_set = table_sets_data['header'] 
    data_set = table_sets_data['data']

    #Team table data (serve to zone per set)
    table_serve_data = prepare_tabulate_serve_data(match, team)
    header_serve = table_serve_data['header']
    data_serve = table_serve_data['data']

    #Team table data (attack to zone per set)
    table_attacks_data = prepare_tabulate_attacks_data(match, team)
    header_attack = table_attacks_data['header']
    data_attack = table_attacks_data['data']

    team_table_data = {
        'header_set':header_set,
        'data_set': data_set,
        'header_serve': header_serve,
        'data_serve': data_serve,
        'header_attack':header_attack,
        'data_attack':data_attack
    }
    return team_table_data

def generate_csv(match, output_file):
    file = output_file+'.csv'
    # general table data
    header = ['Total score']
    data = [[match.team_a, final_set_wins_by_team(match, 'A')], 
        [match.team_b, final_set_wins_by_team(match, 'B')] 
        ]

    team_a_table_data = get_team_table_data(match, 'A')
    team_b_table_data = get_team_table_data(match, 'B')
    sets_data = prepare_table_sets_data(match)
    
    with open(file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)       

        # write multiple rows
        writer.writerows(data)
        writer.writerows('\n')
        writer.writerows('\n')

    # - - - - write Team A data
        writer.writerow(team_a_table_data['header_set'])
        writer.writerows(team_a_table_data['data_set'])
        writer.writerows('\n')

        writer.writerow(team_a_table_data['header_serve'])
        writer.writerows(team_a_table_data['data_serve'])
        writer.writerows('\n')

        writer.writerow(team_a_table_data['header_attack'])
        writer.writerows(team_a_table_data['data_attack'])
        writer.writerows('\n')
        writer.writerows('\n')

    # - - - - write Team B data
        writer.writerow(team_b_table_data['header_set'])
        writer.writerows(team_b_table_data['data_set'])
        writer.writerows('\n')

        writer.writerow(team_b_table_data['header_serve'])
        writer.writerows(team_b_table_data['data_serve'])
        writer.writerows('\n')

        writer.writerow(team_b_table_data['header_attack'])
        writer.writerows(team_b_table_data['data_attack'])
        writer.writerows('\n')
        writer.writerows('\n')

    # - - - - write general set's data
        writer.writerow(sets_data['header_sets'])
        writer.writerows(sets_data['data_sets'])



def convert_csv_to_pdf(output_file):#OVOOO
    csv_file = output_file+'.csv'
    pdf_file=output_file+'.pdf'
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        
        pdf = FPDF()
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin            
        pdf.set_font('Times','B',14.0) 
        pdf.cell(page_width, 0.0, 'Match report', align='C')
        pdf.ln(10)
        pdf.set_font('Courier', '', 12)        
        col_width = page_width/4        
        pdf.ln(10)        
        th = pdf.font_size
        
        for row in reader:
            for r in range(len(row)):
                if row[r] != '\n':
                    pdf.cell(col_width, th, row[r], border=1)
            pdf.ln(th)
        pdf.ln(10)
        pdf.set_font('Times','',10.0) 
        pdf.cell(page_width, 0.0, '- end of report -', align='C')
        pdf.output(pdf_file, 'F')
