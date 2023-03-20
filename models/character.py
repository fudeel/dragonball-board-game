from models.card import Card


class Character:
    _cards = []
    _carrying_spheres = False  # is the current player carrying a dragon ball?
    _card_slot_1 = None
    _card_slot_1_duration = 0
    _card_slot_2 = None
    _card_slot_2_duration = 0

    def __init__(self, name, defense, attack, hp, energy, basic_aoe, pos_x, pos_y):
        self._name = name
        self._defense = defense  # reduces the attack
        self._attack = attack  # reduces hp to the opposite player
        self._hp = hp  # health points
        self._energy = energy  # if maximum can perform special attack. Each turn reloads by 1 unit
        self._basic_aoe = basic_aoe  # area of attack. 1x1, 2x2, 4x4, 8x8. Can also be 30x30 with energy sphere
        self._pos_x = pos_x
        self._pos_y = pos_y

    def __str__(self):
        return f"Character: Name={self._name} Defense={self._defense}, Attack={self._attack}, HP={self._hp}, Energy={self._energy}, Is carrying Dragonball={self._carrying_spheres}, is making AoE={self._basic_aoe}x{self._basic_aoe}, he's in cell: (x: {self._pos_x} y: {self._pos_y}) "

    def get_hp(self):
        return self._hp

    def set_hp(self, hp):
        self._hp = hp

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def move_player(self, new_pos_x, new_pos_y):
        if new_pos_x in range(0, 31) and new_pos_y in range(0, 31):
            self._pos_x = new_pos_x
            self._pos_y = new_pos_y
        else:
            print(f"The movement you're applying to {self._name} is not valid. Please set a valid position")

    def interact_with_trap(self):
        self._hp = self._hp - 1
        return f"HP reduced by 1: {self._hp}"

    def restore_hp(self, qty):
        self._hp = self._hp + qty
        if self._hp > 15:
            self._hp = 15

    def reduce_hp(self, qty):
        self._hp = self._hp - qty

    def restore_energy(self, qty):
        self._energy = self._energy + qty
        if self._energy > 10:
            self._energy = 10

    def reduce_energy(self, qty):
        self._energy = self._energy - qty

    def restore_attack(self, qty):
        self._attack = self._attack + qty

    def reduce_attack(self, qty):
        self._attack = self._attack - qty

    def restore_defense(self, qty):
        self._defense = self._defense + qty

    def reduce_defense(self, qty):
        self._defense = self._defense - qty

    def pick_sphere(self):
        self._carrying_spheres = True

    def drop_sphere(self):
        self._carrying_spheres = False

    def get_pos_x(self):
        return self._pos_x

    def set_pos_x(self, x):
        self._pos_x = x

    def get_pos_y(self):
        return self._pos_y

    def set_pos_y(self, y):
        self._pos_y = y

    def get_carrying_spheres(self):
        return self._carrying_spheres

    def set_carrying_spheres(self, is_drop):
        if is_drop:
            self._carrying_spheres = 0
        else:
            self._carrying_spheres = 1

    def get_defense(self):
        return self._defense

    def set_defense(self, val):
        self._defense = val

    def get_attack(self):
        return self._attack

    def set_attack(self, val):
        print(val)
        self._attack = val

    def get_cards(self):
        return self._cards

    def get_card_by_id(self, card_id) -> Card:
        for c in self._cards:
            if c._id == card_id:
                card = c
                break
        else:
            card = None

        return card

    def set_cards(self, card):
        self._cards.append(card)

    def get_card_slot_1(self) -> Card:
        return self._card_slot_1

    def set_card_slot_1(self, card):
        self._card_slot_1 = card

    def get_card_slot_2(self) -> Card:
        return self._card_slot_2

    def set_card_slot_2(self, card):
        self._card_slot_2 = card

    def get_card_slot_1_duration(self) -> int:
        return self._card_slot_1_duration

    def set_card_slot_1_duration(self, duration):
        self._card_slot_1_duration = duration

    def get_card_slot_2_duration(self) -> int:
        return self._card_slot_2_duration

    def set_card_slot_2_duration(self, duration):
        self._card_slot_2_duration = duration
