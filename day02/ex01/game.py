from collections import Counter
import players as p
from multipledispatch import dispatch


class Game(object):
    def __init__(self, matches=10) -> None:
        self.matches = matches
        self.registry = Counter()

    @dispatch(p.Player, p.Player)
    def play(self, player1: p.Player = None, player2: p.Player = None):
        decision_1 = True
        decision_2 = True
        for i in range(self.matches):
            tmp = decision_1
            decision_1 = player1.is_put_candy(decision_2)
            decision_2 = player2.is_put_candy(tmp)
            if decision_1 is True and decision_2 is True:
                self.registry.update({player1.name: 2, player2.name: 2})
            elif decision_1 is True and decision_2 is False:
                self.registry.update({player1.name: -1, player2.name: 3})
            elif decision_1 is False and decision_2 is True:
                self.registry.update({player1.name: 3, player2.name: -1})

    @dispatch()
    def play(self):
        players = [p.Copycat(), p.Cheater(), p.Cooperator(), p.Grudger(),
                   p.Detective()]  # for match with https://ncase.me/trust/

        for i in range(len(players)):
            for j in range(i + 1, len(players)):
                if players[i].name != players[j].name:
                    players[i].reset_player()
                    players[j].reset_player()
                    self.play(players[i], players[j])

    def top3(self):
        for key, value in self.registry.most_common(3):
            print(key, value)
