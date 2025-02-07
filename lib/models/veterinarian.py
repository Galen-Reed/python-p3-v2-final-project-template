
class Veterinarian:

    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def specialty(self):
        return self._specialty

    @specialty.setter
    def location(self, specialty):
        if isinstance(specialty, str) and len(specialty):
            self._specialty = specialty
        else:
            raise ValueError(
                "Specialty must be a non-empty string"
            )