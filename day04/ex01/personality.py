import random


def gen_trait_score(traits_num: int, score_sum: int):
    for i in range(traits_num):
        score = random.randint(0, score_sum)
        score_sum -= score
        yield score


def gen_traits(traits_list: list) -> dict:
    scores_sum = 100
    traits_dict = {}
    for el in traits_list:
        traits_dict.update({el: 0})
    personality_trait = gen_trait_score(len(traits_list), scores_sum)

    indices = []
    for i in range(len(traits_list)):
        key_id = random.randint(0, len(traits_list) - 1)
        while key_id in indices:
            key_id = random.randint(0, len(traits_list) - 1)
        indices.append(key_id)

    for key_id in indices:
        traits_dict.update({traits_list[key_id]: next(personality_trait)})
    return traits_dict


def turrets_generator():
    traits_list = ["neuroticism", "openness", "conscientiousness",
                   "extraversion", "agreeableness"]
    while True:
        turret_dict = {}
        turret_dict.update(gen_traits(traits_list))

        def shoot():
            print("Shooting")

        def search():
            print("Searching")

        def talk():
            print("Talking")

        actions = {"shoot": shoot, "search": search, "talk": talk}
        turret_dict.update(**actions)

        yield turret_dict


if __name__ == "__main__":
    turrets_factory = turrets_generator()
    turret = next(turrets_factory)

    for key, value in turret.items():
        print(key, end=": ")
        print(value)

    shoot = turret["shoot"]
    search = turret["search"]
    talk = turret["talk"]
    shoot()
    search()
    talk()
