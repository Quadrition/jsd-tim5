
class Set:
    
    def __init__(self, set_num, points) :
        self.set_num = set_num
        self.points = points

    def team_a_points(self):
        count = 0
        for p in self.points:
            if p.team_won_point() == 'A':
                count += 1
        return count

    def team_b_points(self):
        count = 0
        for p in self.points:
            if p.team_won_point() == 'B':
                count += 1
        return count

    