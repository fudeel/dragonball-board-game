class Character:
    def __init__(self, defense, attack, hp, energy, is_carrying_dragonball):
        self.defense = defense
        self.attack = attack
        self.hp = hp
        self.energy = energy
        self.is_carrying_dragonball = is_carrying_dragonball

    def __str__(self):
        return f"Character: Defense={self.defense}, Attack={self.attack}, HP={self.hp}, Energy={self.energy}, Is carrying Dragonball={self.is_carrying_dragonball}"