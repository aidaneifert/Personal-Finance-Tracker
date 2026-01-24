import json
class FinanceTracker():

    def __init__(self):
        self.running= True
        self.input= None
        self.reports= []

        with open('Data.json', 'r') as f: 
            self.reports = json.load(f)

    def user_input(self):
        i = input(">")
        self.input = i.strip()

    def save_to_file(self):
        with open('Data.json', 'w') as f:
            json.dump(self.reports, f, indent= 4)

    def add_income(self):
        id = [d["id"] for d in self.reports]
        if not id:
            new_id = 1
        elif id > 0:
            i= self.reports[-1]
            new_id= i + 1 

        new_type= "income"
        new_amount= input("Amount >")
        new_source=input("Source >")
        new_date=input("Date >")
        new_description=input("Description >")

        new_input ={
        "id":new_id,
        "type":new_type,
        "ammount":new_amount, 
        "source":new_source,
        "date":new_date, 
        "description":new_description
        }
        
        self.reports.append(new_input)
        self.save_to_file()

    def add_expense(self):
        id = [d["id"] for d in self.reports]
        if not id:
            new_id = 1
        elif id > 0:
            i= self.reports[-1]
            new_id= i + 1 

        new_type= "expense"
        new_amount= input("Amount >")
        new_source=input("Source >")
        new_date=input("Date >")
        new_description=input("Description >")

        new_input ={
        "id":new_id,
        "type":new_type,
        "ammount":new_amount, 
        "category":new_source,
        "date":new_date, 
        "description":new_description
        }
        
        self.reports.append(new_input)
        self.save_to_file()

    def show_entries(self):
        for dicts in self.reports:
            for key,transacts in dicts.items():
                print(f"{key}:{transacts}")
        input("Press Enter to exit")
            








    def generate_report(self):
        print("generate report")
        self.user_input()
        i = input("press Enter to continue")
        if i: 
            return

    def edit_entry(self):
        print("Enter a transaction id to edit")
        self.user_input()
        self.input. 
        print(self.input)
        #will need to pop dict from list and keep index, modify values, repack dict, then insert
        #to self.reports

    def remove_entry(self):
        print("remove")
        self.user_input()



    def main_menu(self):
        while self.running: 

            print(("1.Add Income \n"
                   "2.Add Expense \n"
                   "3.Show Entries \n"
                   "4.Generate Report \n"
                   "5.Edit Report \n"
                   "6.Remove Report \n"
                   "7.Exit"))
            self.user_input()

            match self.input:
                case "1":
                    self.add_income()
                case "2":
                    self.add_expense()
                case "3":
                    self.show_entries()
                case "4":
                    self.generate_report()
                case "5":
                    self.edit_entry()
                case "6":
                    self.remove_entry()
                case "7":
                    self.running = False
                case _:
                    print("Invalid input")

if __name__ == "__main__":
    ft = FinanceTracker()
    ft.main_menu() 
