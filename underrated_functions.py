# eval
evaluate_string = '(y*(x+1)) + (y*(x+2))'
x = 5
y = 2
expression = eval(evaluate_string)
print(expression)

# any
lst = [0]
print(any(lst))

lst = [1,0]
print(any(lst))

# vars
class HomeExpensive():

    def __init__(self):
        self.electricity_bill = 10
        self.domain_charges = 15
        self.petty_expensive = 20

home_expensive = HomeExpensive()
print(vars(home_expensive))
