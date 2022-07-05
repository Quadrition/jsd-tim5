class Point:

    def __init__(self, team, serve, assists):
        self.team = team
        self.serve = serve
        self.assists = assists

    def num_of_assists(self):
        return len(self.assists)

    def team_won_point(self):
        
        if len(self.assists) != 0:
            assist = self.assists[-1]
            if assist.actions[0].player.team == 'A':
                return 'B'
            else:
                return 'A'
        elif self.serve.end_of_point == 'ace':
            return self.team
        elif self.team == 'A':
            return 'B'
        else:
            return 'A'
        pass