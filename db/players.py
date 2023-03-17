import sqlite3


def save_players(teams, match_name):
    # Connect to the database
    conn = sqlite3.connect('players.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Create the "players" table if it does not exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS players
                    (id INTEGER PRIMARY KEY,
                    match TEXT,
                     name TEXT,
                     defense INTEGER,
                     attack INTEGER,
                     hp INTEGER,
                     energy INTEGER,
                     carrying_spheres INTEGER,
                     basic_aoe INTEGER,
                     pos_x INTEGER,
                     pos_y INTEGER,
                     team TEXT)''')

    team_puple = teams[0]
    team_orange = teams[1]

    players = team_puple + team_orange

    for player in players:
        p = player.__dict__
        match = match_name
        name = p["name"]
        defense = p["defense"]
        attack = p["attack"]
        hp = p["hp"]
        energy = p["energy"]
        carrying_spheres = p["carrying_spheres"]
        basic_aoe = p["basic_aoe"]
        pos_x = p["pos_x"]
        pos_y = p["pos_y"]

        cursor.execute('''INSERT INTO players (match, name, defense, attack, hp, energy,
        carrying_spheres, basic_aoe, pos_x, pos_y)
                                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (match, name, defense, attack, hp, energy, carrying_spheres, basic_aoe,
                        pos_x, pos_y))

    # Commit the changes to the database
    conn.commit()

    # Close the connection
    conn.close()
