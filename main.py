
from src.model.player import Player
from src.model.point import Point
from src.model.serve import Serve


def test():
    player = Player('A', 10)
    serve = Serve(10, 6, 6, 'ace')
    point = Point('A', serve, [])
    print ( 'Team ',point.team_won_point(), ' wins the point!')

if __name__ == '__main__':
    test()

