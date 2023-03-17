class Character:
    def __init__(self, name, defense, attack, hp, energy, is_carrying_dragonball, basic_aoe, is_playing, pos_x, pos_y):
        self.name = name
        self.defense = defense  # reduces the attack
        self.attack = attack  # reduces hp to the opposite player
        self.hp = hp  # health points
        self.energy = energy  # if maximum can perform special attack. Each turn reloads by 1 unit
        self.is_carrying_dragonball = is_carrying_dragonball  # is the current player carrying a dragon ball?
        self.basic_aoe = basic_aoe  # area of attack. 1x1, 2x2, 4x4, 8x8. Can also be 30x30 with energy sphere
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_playing = is_playing

    def __str__(self):
        return f"Character: Name={self.name} Defense={self.defense}, Attack={self.attack}, HP={self.hp}, Energy={self.energy}, Is carrying Dragonball={self.is_carrying_dragonball}, is making AoE={self.basic_aoe}x{self.basic_aoe}, he's in cell: (x: {self.pos_x} y: {self.pos_y})"

    def move_player(self, dice):
        # Calculate the new position after moving 6 cells
        new_pos_x = min(self.pos_x + dice, 31)  # make sure new row is within the board boundaries
        new_pos_y = min(self.pos_y + dice, 31)  # make sure new column is within the board boundaries
        
        self.pos_x = new_pos_x
        self.pos_y = new_pos_y

    def interact_with_trap(self):
        self.hp = self.hp - 1
        return f"HP reduced by 1: {self.hp}"

    def restore_hp(self, qty):
        self.hp = self.hp + qty
        if self.hp > 15:
            self.hp = 15

    def reduce_hp(self, qty):
        self.hp = self.hp - qty
        if self.hp <= 0:
            self.is_playing = False

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
        self.is_carrying_dragonball = True

    def drop_sphere(self):
        self.is_carrying_dragonball = False
