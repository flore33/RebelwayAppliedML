import random
import string

class RandomNumberUtils:
    """
    Class for generating random numbers
    """
    
    @staticmethod
    def generate_random_id() -> str:
        """
        Generate a random ID of length 6 as a string (uppercase letters only).
        """
        return ''.join(random.choices(string.ascii_uppercase, k=6))
    
#random_id = RandomNumberUtils.generate_random_id()
#print(random_id)

    
    