from S1E9 import Character


class Baratheon(Character):
    """Baratheon class"""
    def __init__(
        self, first_name, is_alive=True):
        """Baratheon constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return self.__stringify(str)

class Lannister(Character):
    """Lannister class"""
    def __init__(
        self, first_name, is_alive=True):
        """Lannister constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, name, is_alive):
        """Function creates Lannister object"""
        return cls(name, is_alive)

