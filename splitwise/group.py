
from split import Split
from equal_split import EqualSplit
from percentage_split import PercentageSplit
from exact_split import ExactSplit
class Group:
    def __init__(self,name, amount):
        self.group_name = name
        self.normal_users_info = []
        self.exact_user_info= []
        self.percent_user_info = []
        self.amount = amount
    
    def add_split(self,Split):
        user = Split.get_user()
        expense_info = Split.get_expense()
        expense = None
        if isinstance(Split,PercentageSplit):
            user_info = {'user' : Split.get_user()
            ,'percentage' : Split.percentage}
            self.percent_user_info.append(user_info)
            return
            
        elif isinstance(Split,EqualSplit):
                user_info = {'user' : Split.get_user()
                ,'equal' : None}
                self.normal_users_info.append(user_info)
                return
        else:
            user_info = {'user' : Split.get_user()
                ,'amount' : Split.get_expense()}
            self.exact_user_info.append(user_info)
            return

        

    def show_all_user_data(self):
        amount = self.amount
        print(f"Groups total amount:- {amount}.\n")
        for user_info in self.exact_user_info:
            user_amount = user_info['amount']
            print(f'User :- {user_info["user"].get_name()} amount :- {user_amount}.\n')
            amount -= user_amount

        for user_info in self.percent_user_info:
            user_amount = (amount * user_info['percentage'])/100
            print(f'User :- {user_info["user"].get_name()} amount :- {user_amount}.\n')
            amount -= user_amount
        if len(self.normal_users_info):
            exact_amount = amount / len(self.normal_users_info)
            for user_info in self.normal_users_info:
                print(f'User :- {user_info["user"].get_name()} amount :- {exact_amount}.\n')
                

