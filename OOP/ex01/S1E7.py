from S1E9 import Character


class Baratheon(Character):
    """Baratheon class"""
    def __init__(
        self, first_name, is_alive=True, family_name="Baratheon", 
        eyes="brown", hairs="dark"
        ):
        """Baratheon constructor"""
        super().__init__(first_name, is_alive)
        self.eyes = eyes
        self.hairs = hairs

class Lannister(Character):
    """Lannister class"""
    def __init__(
        self, first_name, is_alive=True, family_name="Lannister", 
        eyes="blue", hairs="light"
        ):
        """Lannister constructor"""
        super().__init__(first_name, is_alive)

# def create_lannister()
