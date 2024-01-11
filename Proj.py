class Money_Spends :
    def __init__(self,name,category,amount) :
        self.name = name
        self.category = category 
        self.amount = amount
    def __repr__(self):
        return f"<Expense : {self.name}, {self.category}, INR {self.amount:.2f}>"
        