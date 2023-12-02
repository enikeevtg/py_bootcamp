from game import Game
import players as p
import os


def test_strategies_matches(players):
    # print("test_strategies_matches with:",
    #       list(map(lambda p1: p1.name, players)))
    print("***********\ntest_strategies_matches with:")
    for p in players:
        print("\t", p.name)

    game = Game()
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            if players[i].name != players[j].name:
                players[i].reset_player()
                players[j].reset_player()
                game.play(players[i], players[j])
    print("game result:")
    game.top3()


def test_extra_strategy(checking_player, players):
    print("***********\ntest_extra_strategy with:", checking_player.name)
    # print("test_extra_strategy with", checking_player,
    #       "VS", list(map(lambda p1: p1.name, players)))

    if checking_player in players:
        players.remove(checking_player)

    game = Game()
    print("game results:")
    for p2 in players:
        checking_player.reset_player()
        p2.reset_player()
        game.play(checking_player, p2)
        print("\t", checking_player.name, game.registry[checking_player.name],
              ":", game.registry[p2.name], p2.name)
        game.registry.clear()


if __name__ == "__main__":
    os.system('clear')
    players = [p.Cheater(), p.Cooperator(), p.Copycat(), p.Grudger(),
               p.Detective()]
    test_strategies_matches(players)

    extra_player = p.ExtraPlayer()
    players.append(extra_player)
    test_strategies_matches(players)
    test_extra_strategy(extra_player, players)
