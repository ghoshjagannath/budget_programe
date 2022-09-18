from breakup_programe import budget
import datetime


class expense_tracker(budget):
    
    def expense_max(self):
        self.food_amount_limit=budget.expense_limit[0]
        self.cloth_amount_limit=budget.expense_limit[1]
        self.entertainment_amount_limit=budget.expense_limit[2]
        self.rent_amount_limit=budget.expense_limit[3]
        
    
    def expense_track(self):
        type_of_expense=input('Type of expense today?')
        if type_of_expense.lower() not in ["food",'cloth','entertainment','rent']:
            self.expense_track()
        else:
            amount=float(input('Type the amount of expense'))
            remark =input('Description of expense')
            time_now=datetime.datetime.today().isoformat()
            with open("C:/Users/ghosh/AppData/Local/Programs/Python/Python39/Buget_app/notepad.txt",'a+') as f:
                string=type_of_expense+" "+str(amount)+" "+remark+" "+time_now
                f.write(string)
                f.write('\n')
                print('File recorded successfully')
                
                
                



if __name__=="__main__":
    x=expense_tracker()
    x.price_breakup()
    x.expense_max()
        
        
    
    
    
    
