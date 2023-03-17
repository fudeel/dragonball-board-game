class Character:
    def __init__(self, name, defense, attack, hp, energy, carrying_spheres, basic_aoe, pos_x, pos_y):
        self.name = name
        self.defense = defense  # reduces the attack
        self.attack = attack  # reduces hp to the opposite player
        self.hp = hp  # health points
        self.energy = energy  # if maximum can perform special attack. Each turn reloads by 1 unit
        self.carrying_spheres = carrying_spheres  # is the current player carrying a dragon ball?
        self.basic_aoe = basic_aoe  # area of attack. 1x1, 2x2, 4x4, 8x8. Can also be 30x30 with energy sphere
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __str__(self):
        return f"Character: Name={self.name} Defense={self.defense}, Attack={self.attack}, HP={self.hp}, Energy={self.energy}, Is carrying Dragonball={self.carrying_spheres}, is making AoE={self.basic_aoe}x{self.basic_aoe}, he's in cell: (x: {self.pos_x} y: {self.pos_y}) "

    def move_player(self, new_pos_x, new_pos_y):
        if new_pos_x in range(0, 31) and new_pos_y in range(0, 31):
            self.pos_x = new_pos_x
            self.pos_y = new_pos_y
        else:
            print(f"The movement you're applying to {self.name} is not valid. Please set a valid position")

    def interact_with_trap(self):
        self.hp = self.hp - 1
        return f"HP reduced by 1: {self.hp}"

    def restore_hp(self, qty):
        self.hp = self.hp + qty
        if self.hp > 15:
            self.hp = 15

    def reduce_hp(self, qty):
        self.hp = self.hp - qty

    def restore_energy(self, qty):
        self.energy = self.energy + qty
        if self.energy > 10:
            self.energy = 10

    def reduce_energy(self, qty):
        self.energy = self.energy - qty

    def restore_attack(self, qty):
        self.attack = self.attack + qty

    def reduce_attack(self, qty):
        self.attack = self.attack - qty

    def restore_defense(self, qty):
        self.defense = self.defense + qty

    def reduce_defense(self, qty):
        self.defense = self.defense - qty

    def pick_sphere(self):
        self.carrying_spheres = True

    def drop_sphere(self):
        self.carrying_spheres = False

