from group import Group
from split import Split
from user import User
from equal_split import EqualSplit
from percentage_split import PercentageSplit
from exact_split import ExactSplit

user_1 = User('A','abc1@gmail.com')
user_2 = User('B','abc2@gmail.com')
user_3 = User('C','abc3@gmail.com')

group = Group("ABC",100)
split_1 = ExactSplit(user_1,20)
split_2 = EqualSplit(user_2,30)
split_3 = PercentageSplit(user_3,20)
group.add_split(split_1)
group.add_split(split_2)
group.add_split(split_3)
import pdb;pdb.set_trace()
group.show_all_user_data()

# if __main__:

