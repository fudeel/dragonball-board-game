class Card:

    def __init__(self, id, name, desc, tar, eff_code, duration):
        self._id = id  # card id
        self._name = name
        self._description = desc  # card description
        self._target = tar  # card effect's target me | other | cells | all
        self._effect_code = eff_code  # card effect code
        self._duration = duration

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_description(self):
        return self._description

    def set_description(self, desc):
        self._description = desc

    def get_target(self):
        return self._target

    def set_target(self, tar):
        self._target = tar

    def get_effect_code(self):
        return self._effect_code

    def set_effect_code(self, code):
        self._effect_code = code

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration

    def use_card(self):
        if self._effect_code == 000 and self._target == 'me':
            # increase attack power by 1
            return 'attack', 1
        else:
            return []