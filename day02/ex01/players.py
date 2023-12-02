class Player(object):
    name: str = None

    def __init__(self, name: str) -> None:
        self.name = name

    def reset_player(self):
        raise NotImplementedError()

    def is_put_candy(self, opponent_last_decision: bool) -> bool:
        raise NotImplementedError()


class Cheater(Player):
    def __init__(self, name="cheater") -> None:
        super().__init__(name)

    def reset_player(self):
        pass

    def is_put_candy(self, opponent_last_decision: bool) -> bool:
        return False


class Cooperator(Player):
    def __init__(self, name="cooperator") -> None:
        super().__init__(name)

    def reset_player(self):
        pass

    def is_put_candy(self, opponent_last_decision: bool) -> bool:
        return True


class Copycat(Player):
    is_first_round: bool = True

    def __init__(self, name="copycat") -> None:
        super().__init__(name)

    def reset_player(self):
        self.is_first_round = True

    def is_put_candy(self, opponent_last_decision: bool) -> bool:
        if self.is_first_round is True:
            self.is_first_round = False
            return True
        return opponent_last_decision


class Grudger(Player):
    decision: bool = True

    def __init__(self) -> None:
        super().__init__("grudger")

    def reset_player(self):
        self.decision = True

    def is_put_candy(self, opponent_last_decision: bool) -> bool:
        if opponent_last_decision is False:
            self.decision = False
        return self.decision


class Detective(Player):
    current_round: int = 0
    decision: bool = True
    is_cheat_detected: bool = False

    def __init__(self) -> None:
        super().__init__("detective")

    def reset_player(self):
        self.current_round = 0
        self.decision = True
        self.is_cheat_detected = False

    def is_put_candy(self, opponent_last_decision: bool) -> bool:
        self.current_round += 1
        if self.current_round <= 5:
            if opponent_last_decision is False:
                self.is_cheat_detected = True
            if self.current_round == 2:
                return False
            else:
                return True
        if self.is_cheat_detected is True:
            return opponent_last_decision
        else:
            return False


class ExtraPlayer(Player):
    current_round: int = 0
    decision: bool = True
    opponent_strategy: str = ""

    def __init__(self) -> None:
        super().__init__("bang-bang batya v zdanii")

    def reset_player(self):
        self.current_round = 0
        self.decision = True
        self.opponent_strategy = ""

    def is_put_candy(self, opponent_last_decision: bool) -> bool:
        self.current_round += 1
        if self.current_round == 2:
            self.decision = False
            if opponent_last_decision is False:
                self.opponent_strategy = "cheater"

        if self.opponent_strategy == "" and self.current_round == 3:
            self.decision = False
            if opponent_last_decision is False:
                self.opponent_strategy = "detective"
            else:
                self.opponent_strategy = "cooperator, copycat, grudger"

        if self.current_round == 4:
            if self.opponent_strategy == "cooperator, copycat, grudger":
                if opponent_last_decision is True:
                    self.decision = False
                    self.opponent_strategy = "cooperator"
                else:
                    self.decision = True
                    self.opponent_strategy = "copycat or grudger"
            elif self.opponent_strategy == "detective":
                self.decision = True

        if (
          self.current_round == 6 and
          self.opponent_strategy == "copycat or grudger"
        ):
            if opponent_last_decision is False:
                self.decision = False
                self.opponent_strategy = "grudger"
            else:
                self.decision = True
                self.opponent_strategy = "copycat"

        return self.decision
