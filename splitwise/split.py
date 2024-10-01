from user import User

class Split:
    def __init__(self,User):
        self.user = User
        self.amount = 0.0

    def get_user(self):
        return self.user

    def get_expense(self):
        return self.amount
