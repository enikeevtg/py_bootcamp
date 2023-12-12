import random


traits_list = ["neuroticism", "openness", "conscientiousness",
               "extraversion", "agreeableness"]


def gen_trait_score(traits_num: int, score_sum: int):
    for i in range(traits_num - 1):
        score = random.randint(0, score_sum)
        score_sum -= score
        yield score
    yield score_sum


def gen_traits(traits_list: list) -> dict:
    scores_sum = 100
    traits_dict = {}
    for el in traits_list:
        traits_dict.update({el: 0})
    personality_trait = gen_trait_score(len(traits_list), scores_sum)

    key_ids_list = []
    for i in range(len(traits_list)):
        key_id = random.randint(0, len(traits_list) - 1)
        while key_id in key_ids_list:
            key_id = random.randint(0, len(traits_list) - 1)
        key_ids_list.append(key_id)

    for key_id in key_ids_list:
        traits_dict.update({traits_list[key_id]: next(personality_trait)})
    return traits_dict


def turrets_generator(class_name: str = "Turret", traits: list = traits_list):
    parents = (object,)

    while True:
        # fields:
        attributes = gen_traits(traits)

        # methods:
        # def shoot(self):
        #     print("Shooting")

        # def search(self):
        #     print("Searching")

        # def talk(self):
        #     print("Talking")

        # actions = {"shoot": shoot, "search": search, "talk": talk}
        actions = {"shoot": lambda self: print("Shooting"),
                   "search": lambda self: print("Searching"),
                   "talk": lambda self: print("Talking")}
        attributes.update(**actions)

        # for magic method __str__:
        def get_attributes(self):
            sum = (self.neuroticism + self.openness + self.conscientiousness +
                   self.extraversion + self.agreeableness)
            attributes = (f"class: {class_name}\n" +
                          "personality traits: " +
                          f"neuroticism({self.neuroticism}), " +
                          f"openness({self.openness}), " +
                          f"conscientiousness({self.conscientiousness}), " +
                          f"extraversion({self.extraversion}), " +
                          f"agreeableness({self.agreeableness})\n" +
                          f"*scores sum is {sum}\n" +
                          "actions: shoot, search, talk")
            return attributes

        attributes.update({"__str__": get_attributes})

        yield type(class_name, parents, attributes)


if __name__ == "__main__":
    turrets_factory = turrets_generator()
    for i in range(3):
        turret_obj = next(turrets_factory)
        turret = turret_obj()
        print(turret)
        turret.shoot()
        turret.search()
        turret.talk()
        print()
