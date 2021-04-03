
import random
import string

class Robot:

    def __init__(self):
        Robot.reset(self)      

    def reset(self):
        self.name = self.create_name()

    def create_name(self):
        random.seed()
        return "".join(random.sample(string.ascii_uppercase, k =2)) + str(random.randrange(100,999))
        