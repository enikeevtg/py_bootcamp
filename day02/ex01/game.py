from collections import Counter
import players as p


class Game(object):
    def __init__(self, matches=10) -> None:
        self.matches = matches
        self.registry = Counter()

    def play(self, player1: p.Player, player2: p.Player):
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

    def top3(self):
        for key, value in self.registry.most_common(3):
            print(key, value)
