##Create a Budget class that can instantiate objects based on different budget categories like food,
# clothing, and entertainment. These objects should allow for depositing and withdrawing funds from each 
# category, as well computing category balances and transferring balance amounts between categories”



class budget():
    percent=[]
    expense_limit=[]
    def __init__(self):
        self.food=int(input("Type the percentage in decimal manner for food--->"))/100 
        self.clothing=int(input("Type the percentage in decimal manner for clothing--->"))/100 
        self.entertainment=int(input("Type the percentage in decimal manner for entertainment--->"))/100 
        self.rent=int(input("Type the percentage in decimal manner for rent--->"))/100

        if sum((self.food,self.clothing,self.entertainment,self.rent))!=1:
            print('your percentage of breakup of all 4 items is not equal to 100 or 1 in decimal')
            print('So, Type it one time more ')
            self.__init__()
        else:    
            self.percent.extend((self.food,self.clothing,self.entertainment,self.rent))

    
    def price_breakup(self):
        self.total_amount=float(input('Type the total amount of pocket money you have?'))
        self.food_amount=self.total_amount*self.percent[0]
        self.clothing_amount=self.total_amount*self.percent[1]
        self.entertainment_amount=self.total_amount*self.percent[2]
        self.rent_amount=self.total_amount*self.percent[3]

        self.expense_limit.extend((self.food_amount,self.clothing_amount,self.entertainment_amount,self.rent_amount))
        print(self.expense_limit)






















## “Create a lottery ball, or Hat, that takes a variable number of arguments that specify the number of balls of each color 
# that are in the hat. Give the object the ability to pick a random number of balls from the hat, which will then be used to compute the probability 
# of picking a certain distribution of balls over a large number of experiments”

# A Tkinter-based GUI app with SQL database for managing appointments. Check the complete code here.
# Tic Tac Toe: A single-player or multiplayer tic tac toe game using python. Click here to view the source code.
# Tetris: Get the full tutorial and source code for python implementation of Tetris game using pygame GUI here.
# Expense Tracker App: A python application for adding income, and expenses, viewing, and updating details like salary and expenses. Get the source cod