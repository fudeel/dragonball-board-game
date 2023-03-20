from models.character import Character


def character_selection(taken=[]):
    characters = ['goku', 'piccolo', 'crilin', 'gohan', 'vegeta']
    character = ""

    while character not in characters or character in taken:
        character = (input("Select a character [goku] [piccolo] [crilin] [gohan] [vegeta]")).lower()

    if character == 'goku':
        goku = Character(
            name='Goku',
            pos_x=0,
            pos_y=len(taken),
            defense=4,
            energy=8,
            attack=4,
            basic_aoe=2,
            carrying_spheres=0,
            hp=10
        )

        return goku

    if character == 'piccolo':
        piccolo = Character(
            name='Piccolo',
            pos_x=0,
            pos_y=len(taken),
            defense=3,
            energy=10,
            attack=3,
            basic_aoe=2,
            carrying_spheres=0,
            hp=10
        )

        return piccolo

    if character == 'crilin':
        crilin = Character(
            name='Crilin',
            pos_x=0,
            pos_y=len(taken),
            defense=2,
            energy=10,
            attack=2,
            basic_aoe=1,
            carrying_spheres=0,
            hp=10
        )

        return crilin

    if character == 'gohan':
        gohan = Character(
            name='Gohan',
            pos_x=0,
            pos_y=len(taken),
            defense=2,
            energy=15,
            attack=3,
            basic_aoe=1,
            carrying_spheres=0,
            hp=10
        )

        return gohan

    if character == 'vegeta':
        vegeta = Character(
            name='Vegeta',
            pos_x=0,
            pos_y=len(taken),
            defense=3,
            energy=10,
            attack=5,
            basic_aoe=2,
            carrying_spheres=0,
            hp=10
        )

        return vegeta
