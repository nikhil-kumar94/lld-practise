from split import Split
from user import User
class PercentageSplit(Split):
    def __init__(self, User, percentage):
        super().__init__(User)
        self.percentage = percentage


    def get_expense(self):
        return 'percentage'