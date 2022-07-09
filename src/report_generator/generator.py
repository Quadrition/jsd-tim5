
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
    
    data = []
    header = ['Team '+ team_name , 'points', 'serve error','serve ace']
    for i in range(len(match.sets)):
        num = i+1
        set_data = prepare_set_data_per_team(match.sets[i], team)
        data.append(['Set '+str(num), set_data['points'], set_data['serve_err'],set_data['serve_ace']])
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

    data_attack = []
    header_attack = ['Team '+ team_name , 'Set1', 'Set 2','Set 3']
    for zone in [1,2,3,4,5,6]:
        data_attack.append(['Attack to zone '+str(zone)])
        for i in range(len(match.sets)):
            set_attacks = prepare_attacks_data(match.sets[i], team)
            data_attack[zone-1].append(set_attacks['zone'+str(zone)])

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

    data_serve = []
    header_serve = ['Team '+ team_name , 'Set1', 'Set 2','Set 3']
    for zone in [1,2,3,4,5,6]:
        data_serve.append(['Attack to zone '+str(zone)])
        for i in range(len(match.sets)):
            set_attacks = prepare_serve_data(match.sets[i], team)
            data_serve[zone-1].append(set_attacks['zone'+str(zone)])

    table_data = {
        'header':header_serve,
        'data':data_serve
    } 
    return table_data

def prepare_table_sets_data(match):
    header_sets = ['','longest rally','average rally']
    data_sets = []
    for i in range(len(match.sets)):
        set_num = i+1
        data_sets.append(['Set '+str(set_num), longest_rally_for_set(match.sets[i]), average_rally_for_set(match.sets[i])])

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



def convert_csv_to_pdf(output_file):
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


def generate_report(source_file, output_file):
    model = interpreter(source_file)
    match = create_model(model)
    generate_csv(match, output_file)
    convert_csv_to_pdf(output_file)


if __name__ == '__main__':
    print('Please wait...')

    source_file = join('..', sys.argv[1])
    output_file = sys.argv[2]
    generate_report(source_file,output_file)
    print('Report generated.')
