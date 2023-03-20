class Card:

    def __init__(self, id, desc, tar):
        self._id = id  # card id
        self._description = desc  # card description
        self._target = tar  # card effect's target me | other | cells | all

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
