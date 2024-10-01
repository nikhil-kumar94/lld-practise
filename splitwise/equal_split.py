from split import Split
from user import User
class EqualSplit(Split):
    def __init__(self, User, amount):
        super().__init__(User)


    def get_expense(self):
        return 'exact'