class Character:
    def __init__(self, name, defense, attack, hp, energy, is_carrying_dragonball, basic_aoe, current_pos):
        self.name = name
        self.defense = defense  # reduces the attack
        self.attack = attack  # reduces hp to the opposite player
        self.hp = hp  # health points
        self.energy = energy  # if maximum can perform special attack. Each turn reloads by 1 unit
        self.is_carrying_dragonball = is_carrying_dragonball  # is the current player carrying a dragon ball?
        self.basic_aoe = basic_aoe  # area of attack. 1x1, 2x2, 4x4, 8x8. Can also be 30x30 with energy sphere
        self.current_pos = current_pos  # position in the board

    def __str__(self):
        return f"Character: Name={self.name} Defense={self.defense}, Attack={self.attack}, HP={self.hp}, Energy={self.energy}, Is carrying Dragonball={self.is_carrying_dragonball}, is making AoE={self.basic_aoe}x{self.basic_aoe}"
