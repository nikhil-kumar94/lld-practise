from split import Split
from user import User
class ExactSplit(Split):
    def __init__(self, User, amount):
        super().__init__(User)
        self.amount = amount
    
    def get_expense(self):
        return self.amount
