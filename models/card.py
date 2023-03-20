class Card:

    def __init__(self, id, desc, tar, eff_code):
        self._id = id  # card id
        self._description = desc  # card description
        self._target = tar  # card effect's target me | other | cells | all
        self._effect_code = eff_code  # card effect code

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

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