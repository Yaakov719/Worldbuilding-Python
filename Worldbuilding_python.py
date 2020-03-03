import random
from time import sleep


def flip_a_coin(x):
    coin = random.randint(0, 1)
    if x == 0:
        return coin
    if x > 0:
        if coin == 0:
            return False
        if coin == 1:
            return True


class Star:

    def __init__(self, classification, mass, radius, temp, habitable, planet):
        self.type = classification
        self.mass = mass
        self.radius = radius
        self.temp = temp
        self.habitable = habitable
        self.planet = planet


class Binary:

    def __init__(self, primary, secondary, orbit_type, habitable, orbit):
        self.primary = primary
        self.secondary = secondary
        self.orbit_type = orbit_type
        self.habitable = habitable
        self.orbit = orbit


class Orbit:

    def __init__(self, dist, eccentricity, min_sep, max_sep):
        self.dist = dist
        self.eccentricity = eccentricity
        self.min_sep = min_sep
        self.max_sep = max_sep


class Planet:

    def __init__(self, kind, dist):
        self.type = kind
        self.dist = dist


def derprershurn():
    if star_count == 1:
        throw(system[0].primary, 0)
    if star_count == 2 and system[0].orbit_type == 1 and system[0].primary.type in "O B A F G K M" and \
            system[0].secondary.type in "O B A F G K M":
        o = Star("h", pow((pow(system[0].primary.mass, 3) + pow(system[0].secondary.mass, 3)), (1 / 3)),
                 system[0], system[0].primary.mass + system[0].secondary.mass, "no", [])
        throw(o, 0)
        star_list.insert(2, o)
    elif star_count == 2 and system[0].orbit_type == 2:
        throw(system[0].primary, 1)
        throw(system[0].secondary, 1)
    if star_count == 3:
        if system[0].primary.orbit_type == 1 and system[0].primary.primary.type in "O B A F G K M" and \
                system[0].primary.secondary.type in "O B A F G K M":
            o = Star("h", pow((pow(system[0].primary.primary.mass, 3) + pow(system[0].primary.secondary.mass, 3)),
                              (1 / 3)), system[0].primary, system[0].primary.primary.mass +
                     system[0].primary.secondary.mass, "no", [])
            throw(o, 0)
            star_list.insert(3, o)
        elif system[0].primary.orbit_type == 2:
            throw(system[0].primary.primary, 2)
            throw(system[0].primary.secondary, 2)
        throw(system[0].secondary, 0)
    if star_count == 4:
        if system[0].primary.orbit_type == 1 and system[0].primary.primary.type in "O B A F G K M" and \
                system[0].primary.secondary.type in "O B A F G K M":
            o = Star("h",
                     pow((pow(system[0].primary.primary.mass, 3) + pow(system[0].primary.secondary.mass, 3)), (1 / 3)),
                     system[0].primary, system[0].primary.primary.mass + system[0].primary.secondary.mass, "no", [])
            throw(o, 0)
            star_list.insert(4, o)
        elif system[0].primary.orbit_type == 2:
            throw(system[0].primary.primary, 2)
            throw(system[0].primary.secondary, 2)
            o = Star("no", "star", "here", "please", "try", "again")
            star_list.insert(4, o)

        if system[0].secondary.orbit_type == 1 and system[0].secondary.primary.type in "O B A F G K M" and \
                system[0].secondary.secondary.type in "O B A F G K M":
            o = Star("h", pow((pow(system[0].secondary.primary.mass, 3) + pow(system[0].secondary.secondary.mass, 3)),
                              (1 / 3)), system[0].secondary, system[0].secondary.primary.mass +
                     system[0].secondary.secondary.mass, "no", [])
            throw(o, 0)
            star_list.insert(5, o)
        elif system[0].secondary.orbit_type == 2:
            throw(system[0].secondary.primary, 3)
            throw(system[0].secondary.secondary, 3)


def throw(x, far):
    inner = 0
    outer = 0
    ooner = 0
    ooter = 0
    oooter = 4000
    i_1 = 0

    if str(x.type) in "O B A F G K M h":
        fred = pow(x.mass, 1.5) * 4.85
        initiate = (random.randint(0, 120) / 100)
        fred += initiate
        fled = fred
        r_2 = (random.randint(140, 200) / 100)
        if far == 0:
            if x.type not in "h":
                inner = x.mass * 0.1
                outer = x.mass * 40
                ooner = 0
                ooter = x.mass * 40
            if x.type == "h":
                inner = x.temp * 0.1
                outer = x.temp * 40
                ooner = x.radius.orbit.max_sep * 3
                ooter = x.temp * 40
        if far >= 1:
            inner = x.mass * 0.1
            outer = x.mass * 40
            ooner = 0
        if far == 1:
            ooter = system[0].orbit.min_sep / 3
        if far == 2:
            ooter = system[0].primary.orbit.min_sep / 3
        if far == 3:
            ooter = system[0].secondary.orbit.min_sep / 3
        if star_count > 2:
            oooter = system[0].orbit.min_sep / 3

        planet = Planet("Jupiter", fred)
        if fred < outer and fred < ooter and fred < oooter:
            x.planet.append(planet)

        while fred < outer and fred < ooter and fred < oooter:
            fred *= r_2
            r_2 = (random.randint(140, 200) / 100)
            planet = Planet("Gas Giant", fred)
            if fred < outer and fred < ooter and fred < oooter:
                x.planet.append(planet)

        if x.type in "O B A F G K M h":
            while fled > inner and fled > ooner:
                r_2 = (random.randint(140, 200) / 100)
                fled /= r_2
                planet = Planet("Terrestrial", fled)
                if fled > inner and fled > ooner:
                    x.planet.insert(0, planet)
        for a in range(len(x.planet)):
            if x.planet[i_1].dist < inner or x.planet[i_1].dist < ooner or x.planet[i_1].dist > outer or \
                    x.planet[i_1].dist > ooter or x.planet[i_1].dist > oooter:
                del x.planet[i_1]
            else:
                i_1 += 1


def swing(x, y, orbit_type):
    hold = 15
    please = 70
    a = 0
    b = 0
    c = 0
    d = 0
    while c < 0.1:
        if orbit_type == 1:
            a = (random.randint(int(hold), 60) / 100)
        elif orbit_type == 2:
            a = (random.randint(15000, 60000) / 100)
        else:
            a = random.randint(15000, 60000)
        b = (random.randint(40, int(please)) / 100)

        c = ((a * (y.mass / (x.mass + y.mass))) * (1 - b)) + ((a - (a * (y.mass / (x.mass + y.mass)))) * (1 - b))
        d = ((a * (y.mass / (x.mass + y.mass))) * (1 + b)) + ((a - (a * (y.mass / (x.mass + y.mass)))) * (1 + b))
        hold += 1
        please -= 1

    return Orbit(a, b, c, d)


def switch(x, y, z):
    x[y], x[z] = x[z], x[y]


def arrange_pairs(x):
    if star_count == 4:
        a = random.randint(1, 2)
        b = random.randint(1, 2)
        c = Star("no", (x[0].mass + x[1].mass), "no", "no", "no", "no")
        d = Star("no", (x[2].mass + x[3].mass), "no", "no", "no", "no")
        e = False
        f = False
        if a == 1:
            if x[0].type in "F G K M":
                if x[1].type in "F G K M":
                    e = True
                    x[0].habitable = True
                    x[1].habitable = True
        elif x[0].habitable or x[1].habitable:
            e = True
        elif a == 2:
            e = False

        if b == 1:
            if x[2].type in "F G K M":
                if x[3].type in "F G K M":
                    f = True
                    x[2].habitable = True
                    x[3].habitable = True
        elif x[2].habitable or x[3].habitable:
            f = True
        elif b == 2:
            f = False

        if e or f:
            g = True
        else:
            g = False

        binary_bond_1 = Binary(x[0], x[1], a, e, swing(x[0], x[1], a))
        binary_bond_2 = Binary(x[2], x[3], b, f, swing(x[2], x[3], b))
        binary_of_binaries = Binary(binary_bond_1, binary_bond_2, 3, g, swing(c, d, 3))
        system.insert(0, binary_of_binaries)

    elif star_count == 3:
        a = random.randint(1, 2)
        d = Star("no", (x[0].mass + x[1].mass), "no", "why", "no", "no")
        e = False
        h = False
        if a == 1:
            if x[0].type in "F G K M":
                if x[1].type in "F G K M":
                    e = True
                    x[0].habitable = True
                    x[1].habitable = True
        elif x[0].habitable or x[1].habitable:
            e = True
        elif a == 2:
            e = False

        binary_bond = Binary(x[0], x[1], a, e, swing(x[0], x[1], a))

        if binary_bond.habitable or x[2].habitable:
            h = True

        bin_and_a_star = Binary(binary_bond, x[2], 3, h, swing(d, x[2], 3))
        system.insert(0, bin_and_a_star)

    elif star_count == 2:
        a = random.randint(1, 2)
        e = False
        if a == 1:
            if x[0].type in "F G K M":
                if x[1].type in "F G K M":
                    e = True
                    x[0].habitable = True
                    x[1].habitable = True
        elif x[0].habitable or x[1].habitable:
            e = True
        elif a == 2:
            e = False
        binary_bond = Binary(x[0], x[1], a, e, swing(x[0], x[1], a))
        system.insert(0, binary_bond)

    elif star_count == 1:
        binary_bond = Binary(x[0], x[0], 0, x[0].habitable, "No Orbital Info")
        system.insert(0, binary_bond)


def sort_by_mass(x):
    if len(x) == 2 and x[0].mass < x[1].mass:
        switch(x, 0, 1)
    elif len(x) == 3:
        if x[0].mass < x[1].mass:
            switch(x, 0, 1)
        if x[1].mass < x[2].mass:
            switch(x, 1, 2)
        if x[0].mass < x[1].mass:
            switch(x, 0, 1)
    elif len(x) == 4:
        if x[0].mass < x[1].mass:
            switch(x, 0, 1)
        if x[1].mass < x[2].mass:
            switch(x, 1, 2)
        if x[2].mass < x[3].mass:
            switch(x, 2, 3)
        if x[0].mass < x[1].mass:
            switch(x, 0, 1)
        if x[1].mass < x[2].mass:
            switch(x, 1, 2)
        if x[0].mass < x[1].mass:
            switch(x, 0, 1)


def black_hole_mass_generator():
    black_hole_number = 0
    while True:
        coin = random.randint(0, 1)
        if coin == 0:
            coin = False
        if coin == 1:
            coin = True
        if coin:
            black_hole_number += 1
        if not coin:
            return (random.randint(500 * black_hole_number + 500, 500 * black_hole_number + 1500)) / 100


def sprint(x):
    print(f"Star Type: {x.type}\n"
          f"Mass: {x.mass}\n"
          f"Radius: {x.radius}")


def sliv(staar, planet):
    print(f"{star_list[staar].planet[planet].type}: {star_list[staar].planet[planet].dist} AU")


test = 0

for i in range(10000000):  # How many times we run the program, note that trying to see more than 10,000 systems at a
    # time will usually overfill the terminal below.

    repeater = 0
    star_type = 0
    star_mass = 0
    star_radius = 0
    star_list = []
    Habitable = False
    system = []

    var_0 = random.randint(1, 1000)
    if var_0 <= 900:
        star_count = 1
    elif var_0 <= 990:
        star_count = 2
    elif var_0 <= 999:
        star_count = 3
    else:
        star_count = 4

    while repeater < star_count:
        var_1 = random.randint(1, 10000)
        if var_1 <= 7645:
            star_type = "M"
            star_mass = random.randint(8, 45) / 100
            Habitable = False
        elif var_1 <= 8855:
            star_type = "K"
            star_mass = random.randint(45, 80) / 100
            Habitable = True
        elif var_1 <= 9615:
            star_type = "G"
            star_mass = random.randint(80, 104) / 100
            Habitable = True
        elif var_1 <= 9915:
            star_type = "F"
            star_mass = random.randint(104, 140) / 100
            Habitable = True
        elif var_1 <= 9975:
            star_type = "A"
            star_mass = random.randint(140, 210) / 100
            Habitable = False
        elif var_1 <= 9988:
            star_type = "B"
            star_mass = random.randint(210, 1600) / 100
            Habitable = False
        elif var_1 <= 9997:
            star_type = "O"
            star_mass = random.randint(1600, 10000) / 100
            Habitable = False
        elif var_1 == 9998:
            star_type = "White Dwarf"
            star_mass = random.randint(17, 140) / 100
            star_radius = pow(star_mass, -(1 / 3))
            Habitable = False
        elif var_1 == 9999:
            star_type = "Neutron Star"
            star_mass = random.randint(140, 300) / 100
            star_radius = random.randint(10, 13) / 695510
            Habitable = False
        else:
            star_type = "Black Hole"
            star_mass = black_hole_mass_generator()
            star_radius = (2.95 * star_mass) / 695510
            Habitable = False

        if star_type in "O B A F G K M":
            star_radius = pow(star_mass, 0.74)

        star = Star(star_type, star_mass, star_radius, pow(star_mass, 0.505), Habitable, [])

        star_list.append(star)

        repeater += 1

    if star_count > 1:
        sort_by_mass(star_list)

    arrange_pairs(star_list)

    if True:  # The Great Filter

        derprershurn()

        for star in system:
            if star_count >= 1:
                if star_count == 1:
                    j = "Single Star"
                else:
                    j = "Primary Star"
                print(f"Number of stars: {star_count}\n"
                      f"\n"
                      f"{j}")
                sprint(star_list[0])

                if star_count == 1:
                    print(f"\n"
                          f"\n"
                          f"\n")
                if star_count >= 2 and star.orbit_type == 1:
                    print(f"|\n"
                          f"|")
                elif star_count > 2 and star.primary.orbit_type == 1:
                    print(f"|\n"
                          f"|")
                elif star_count == 2 and star.orbit_type == 2:
                    print(f"\n"
                          f"\n")
                elif star_count > 2 and star.primary.orbit_type == 2:
                    print(f"\n"
                          f"\n")

            if star_count >= 2:
                print(f"Secondary Star")
                sprint(star_list[1])

                if star_count == 2:
                    print(f"\n"
                          f"\n"
                          f"\n")
                else:
                    print(f"\n"
                          f"\n")

            if star_count >= 3:
                print(f"Tertiary Star")
                sprint(star_list[2])

                if star_count == 3:
                    print(f""
                          f"\n"
                          f"\n"
                          f"\n")
                elif star_count == 4 and star.secondary.orbit_type == 1:
                    print(f"|\n"
                          f"|")
                elif star_count == 4 and star.secondary.orbit_type == 2:
                    print(f"\n"
                          f"\n")

            if star_count == 4:
                print(f"Quad Star")
                sprint(star_list[3])

                print(f"\n"
                      f"\n"
                      f"\n")

        while True:  # Information Library, also enables One System At A Time Mode when set to True.

            j = input(">>")

            if j.lower() == "help":
                print(f"What I have so far:"
                      f"\n"
                      f"Orbital Info on the following binary bonds can be accessed by typing 1 through 3, as shown\n"
                      f"\n"
                      f"       1       3\n"
                      f"'1' -> |-------| <- '2'\n"
                      f"       2   ^   4\n"
                      f"          '3'\n"
                      f"\n"
                      f" You can access information about planets in the system by typing 'Star'. \n"
                      f" The system will ask 'Which one?' to which you can type 2 for the 2nd star in the system.\n"
                      f" Then, type 1 for the closest planet to the star, 2 for the 2nd, ETC.\n"
                      f"\n"
                      f" You can also type '#' and select a star to get a list of orbiting planets.")

            if j.lower() == "next":
                break

            if star_count == 1:
                if j in "123":
                    print(f"No Orbital Info")

            if star_count == 2:
                if j == "1":
                    print(f"Primary and Secondary Stars Orbital Info:\n"
                          f"\n"
                          f"Average distance: {system[0].orbit.dist} AU\n"
                          f"Eccentricity: {system[0].orbit.eccentricity}\n"
                          f"Minimum separation: {system[0].orbit.min_sep}\n"
                          f"Maximum separation: {system[0].orbit.max_sep}\n")
                elif j in "23":
                    print(f"No Orbital Info")

            elif star_count == 3:
                if j == "1":
                    print(f"Primary and Secondary Stars Orbital Info:\n"
                          f"\n"
                          f"Average distance: {system[0].primary.orbit.dist} AU\n"
                          f"Eccentricity: {system[0].primary.orbit.eccentricity}\n"
                          f"Minimum separation: {system[0].primary.orbit.min_sep}\n"
                          f"Maximum separation: {system[0].primary.orbit.max_sep}\n")
                if j == "3":
                    print(f"Binary Pair's and Tertiary Stars Orbital Info:\n"
                          f"\n"
                          f"Average distance: {system[0].orbit.dist} AU\n"
                          f"Eccentricity: {system[0].orbit.eccentricity}\n"
                          f"Minimum separation: {system[0].orbit.min_sep}\n"
                          f"Maximum separation: {system[0].orbit.max_sep}\n")
                if j == "2":
                    print(f"No Orbital Info")

            elif star_count == 4:
                if j == "1":
                    print(f"Primary and Secondary Stars Orbital Info:\n"
                          f"\n"
                          f"Average distance: {system[0].primary.orbit.dist} AU\n"
                          f"Eccentricity: {system[0].primary.orbit.eccentricity}\n"
                          f"Minimum separation: {system[0].primary.orbit.min_sep}\n"
                          f"Maximum separation: {system[0].primary.orbit.max_sep}\n")
                if j == "2":
                    print(f"Tertiary and Quad Stars Orbital Info:\n"
                          f"\n"
                          f"Average distance: {system[0].secondary.orbit.dist} AU\n"
                          f"Eccentricity: {system[0].secondary.orbit.eccentricity}\n"
                          f"Minimum separation: {system[0].secondary.orbit.min_sep}\n"
                          f"Maximum separation: {system[0].secondary.orbit.max_sep}\n")
                if j == "3":
                    print(f"Binary Systems' Mega-Orbit Info:\n"
                          f"\n"
                          f"Average distance: {system[0].orbit.dist} AU\n"
                          f"Eccentricity: {system[0].orbit.eccentricity}\n"
                          f"Minimum separation: {system[0].orbit.min_sep}\n"
                          f"Maximum separation: {system[0].orbit.max_sep}\n")

            if j.lower() == "star":
                print("Which one?")
                k = int(input(">>"))
                if k > len(star_list) or k < 1:
                    print("Error, please try again.")
                else:
                    print("Select a planet.")
                    j = int(input(">>"))
                    if star_count == 1:
                        if j > len(star_list[k - 1].planet):
                            print("THERE AIN'T THAT MANY PLANETS JIMBO\n")
                        else:
                            sliv(k - 1, j - 1)
                    elif star_count == 2:
                        if system[0].orbit_type == 1:
                            if j > len(star_list[2].planet):
                                print("THERE AIN'T THAT MANY PLANETS JIMBO\n")
                            else:
                                sliv(2, j - 1)
                        elif system[0].orbit_type == 2:
                            if j > len(star_list[k - 1].planet):
                                print("THERE AIN'T THAT MANY PLANETS JIMBO\n")
                            else:
                                sliv(k - 1, j - 1)
                    elif star_count == 3:
                        if k == 3:
                            if j > len(star_list[2].planet):
                                print("THERE AIN'T THAT MANY PLANETS JIMBO\n")
                            else:
                                sliv(2, j - 1)
                        elif system[0].primary.orbit_type == 1:
                            if j > len(star_list[3].planet):
                                print("THERE AIN'T THAT MANY PLANETS JIMBO\n")
                            else:
                                sliv(3, j - 1)
                        elif system[0].primary.orbit_type == 2:
                            if j > len(star_list[k - 1].planet):
                                print("THERE AIN'T THAT MANY PLANETS JIMBO\n")
                            else:
                                sliv(k - 1, j - 1)
                    elif star_count == 4:
                        if system[0].primary.orbit_type == 1 and system[0].secondary.orbit_type == 1:
                            if str(k) in "12":
                                if j > len(star_list[4].planet):
                                    print("THERE AIN'T THAT MANY PLANETS JIMBO\n")
                                else:
                                    sliv(4, j - 1)
                            elif str(k) in "34":
                                if j > len(star_list[5].planet):
                                    print("THERE AIN'T THAT MANY PLANETS JIMBO\n")
                                else:
                                    sliv(5, j - 1)
                            else:
                                print("Error, please try again.")
                        elif system[0].primary.orbit_type == 1 and system[0].secondary.orbit_type == 2:
                            if str(k) in "12":
                                if j > len(star_list[4].planet):
                                    print("THERE AIN'T THAT MANY PLANETS JIMBO\n")
                                else:
                                    sliv(4, j - 1)
                            elif str(k) in "34":
                                if j > len(star_list[k - 1].planet):
                                    print("THERE AIN'T THAT MANY PLANETS JIMBO\n")
                                else:
                                    sliv(k - 1, j - 1)
                            else:
                                print("Error, please try again.")
                        elif system[0].primary.orbit_type == 2 and system[0].secondary.orbit_type == 1:
                            if str(k) in "12":
                                if j > len(star_list[k - 1].planet):
                                    print("THERE AIN'T THAT MANY PLANETS JIMBO\n")
                                else:
                                    sliv(k - 1, j - 1)
                            elif str(k) in "34":
                                if j > len(star_list[5].planet):
                                    print("THERE AIN'T THAT MANY PLANETS JIMBO\n")
                                else:
                                    sliv(5, j - 1)
                            else:
                                print("Error, please try again.")
                        elif system[0].primary.orbit_type == 2 and system[0].secondary.orbit_type == 2:
                            if j > len(star_list[k - 1].planet):
                                print("THERE AIN'T THAT MANY PLANETS JIMBO\n")
                            else:
                                sliv(k - 1, j - 1)
                        else:
                            print("I don't know what you did, but you completely broke the system.\n"
                                  "I'm somewhat proud of you.")
            elif j.lower() == "#":
                print("Select a star:")
                k = int(input(">>"))
                if k > len(star_list) or k < 1:
                    print("Error, please try again.")
                elif star_count == 1:
                    print(f"Planets: "
                          f"{len(star_list[0].planet)}\n"
                          f"\n")
                    for Celest in system[0].primary.planet:
                        print(f"Type: {Celest.type}\n"
                              f"Distance: {Celest.dist} AU\n")
                elif star_count > 1:
                    print(f"Planets: ")
                    if star_count == 2 and system[0].orbit_type == 1:
                        print(f"{len(star_list[2].planet)}\n"
                              f"\n")
                        for Celest in star_list[2].planet:
                            print(f"Type: {Celest.type}\n"
                                  f"Distance: {Celest.dist} AU\n")
                    elif star_count == 3 and system[0].primary.orbit_type == 1 and k < 3:
                        print(f"{len(star_list[3].planet)}\n"
                              f"\n")
                        for Celest in star_list[3].planet:
                            print(f"Type: {Celest.type}\n"
                                  f"Distance: {Celest.dist} AU\n")
                    elif star_count == 4 and system[0].primary.orbit_type == 1 and k < 3:
                        print(f"{len(star_list[4].planet)}\n"
                              f"\n")
                        for Celest in star_list[4].planet:
                            print(f"Type: {Celest.type}\n"
                                  f"Distance: {Celest.dist} AU\n")
                    elif star_count == 4 and system[0].secondary.orbit_type == 1 and k > 2:
                        print(f"{len(star_list[5].planet)}\n"
                              f"\n")
                        for Celest in star_list[5].planet:
                            print(f"Type: {Celest.type}\n"
                                  f"Distance: {Celest.dist} AU\n")
                    else:
                        print(f"{len(star_list[k - 1].planet)}\n"
                              f"\n")
                        for Celest in star_list[k - 1].planet:
                            print(f"Type: {Celest.type}\n"
                                  f"Distance: {Celest.dist} AU\n")

        test += 1

print(f"{test} passed!")


sleep(1000)

