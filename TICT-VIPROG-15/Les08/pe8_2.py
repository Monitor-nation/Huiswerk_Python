import random


def monopolyworp():
    aantal_dubbel = 0

    while aantal_dubbel < 3:
        steen_1 = random.randrange(1, 10)
        steen_2 = random.randrange(1, 10)

        if steen_1 != steen_2:
            print("{} + {} = {}".format(steen_1, steen_2, steen_1 + steen_2))
            break
        else:
            aantal_dubbel = aantal_dubbel + 1
            if aantal_dubbel == 3:
                print("{} + {} = {} (direct naar gevangenis)".format(steen_1, steen_2, steen_1 + steen_2))
            else:
                print("{} + {} = {} (dubbel)".format(steen_1, steen_2, steen_1 + steen_2))


monopolyworp()