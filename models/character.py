class Character:
    def __init__(self, name, defense, attack, hp, energy, is_carrying_dragonball, basic_aoe, pos_x, pos_y):
        self.name = name
        self.defense = defense  # reduces the attack
        self.attack = attack  # reduces hp to the opposite player
        self.hp = hp  # health points
        self.energy = energy  # if maximum can perform special attack. Each turn reloads by 1 unit
        self.is_carrying_dragonball = is_carrying_dragonball  # is the current player carrying a dragon ball?
        self.basic_aoe = basic_aoe  # area of attack. 1x1, 2x2, 4x4, 8x8. Can also be 30x30 with energy sphere
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __str__(self):
        return f"Character: Name={self.name} Defense={self.defense}, Attack={self.attack}, HP={self.hp}, Energy={self.energy}, Is carrying Dragonball={self.is_carrying_dragonball}, is making AoE={self.basic_aoe}x{self.basic_aoe}, he's in cell: (x: {self.pos_x} y: {self.pos_y})"

    def interact_with_trap(self):
        self.hp = self.hp - 1
        return f"HP reduced by 1: {self.hp}"
