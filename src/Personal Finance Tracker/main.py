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
        id = [d["id"] for d in self.reports]  #forgot how this works/ look into this. 
   
        if not id:
            new_id = 1
        else:
            i= len(self.reports)
            new_id= i + 1

        new_type= "income"
        new_amount= input("Amount >")
        new_source=input("Source >")
        new_date=input("Date >")
        new_description=input("Description >")

        new_input ={
        "id":new_id,
        "type":new_type,
        "amount":new_amount, 
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
        else:
            i= len(self.reports)
            new_id= i + 1

        new_type= "expense"
        new_amount= input("Amount >")
        new_category=input("Category >")
        new_date=input("Date >")
        new_description=input("Description >")

        new_input ={
        "id":new_id,
        "type":new_type,
        "amount":new_amount, 
        "category":new_category,
        "date":new_date, 
        "description":new_description
        }
        
        self.reports.append(new_input)
        self.save_to_file()

    def show_entries(self):
        for dicts in self.reports:
            for key,transacts in dicts.items():
                print(f"{key}:{transacts}")
        print("\ntype e to edit, type r to remove, press enter to exit")
        self.user_input()
        i = self.input.lower()
        match i:
            case "e":
                self.edit_entry()
            case "r":
                self.remove_entry()
            case "":
                return 
            case _: 
                print("Invalid input")

    def generate_report(self):
        pass

    def edit_entry(self):
        print("Enter a transaction id to edit") 
        self.user_input()

        try:
            to_remove = int(self.input)
        except ValueError:
            print("Invalid Input")
        
        for i, d in enumerate(self.reports):
            if d.get("id") == to_remove:
                entry = self.reports.pop(i)

        dict_id= entry.get("id")
        dict_type=  entry.get("type")

        match dict_type:
            case "expense":
                amount= entry.get("ammount")
                category= entry.get("category")
                date= entry.get("date")
                description= entry.get("description")

                new_amount= input(f"Previous value: {amount} >")
                new_category= input(f"Previous value: {category} >")
                new_date= input(f"Previous value: {date} >")
                new_description= input(f"Previous value: {description} >")

                new_input ={
                "id":dict_id,
                "type":dict_type,
                "amount":new_amount, 
                "category":new_category,
                "date":new_date, 
                "description":new_description
                }

            case "income":
                amount= entry.get("ammount")
                source= entry.get("source")
                date= entry.get("date")
                description= entry.get("description")

                new_amount= input(f"Previous value: {amount} >")
                new_source= input(f"Previous value: {source} >")
                new_date= input(f"Previous value: {date} >")
                new_description= input(f"Previous value: {description} >")

                new_input={
                "id":dict_id,
                "type":dict_type,
                "amount":new_amount, 
                "source":new_source,
                "date":new_date,
                "description":new_description
                }

        self.reports.insert(i, new_input)
        self.save_to_file()

    def remove_entry(self):
        print("Enter a transaction id to remove") 
        self.user_input()

        try:
            input = int(self.input)
        except ValueError:
            print("Invalid input")

        for i, d in enumerate(self.reports):
            if d.get("id") == input:
                self.reports.pop(i)
                self.save_to_file()

    def main_menu(self):
        while self.running: 

            print(("1.Add Income \n"
                   "2.Add Expense \n"
                   "3.Show/Edit Entries \n"
                   "4.Generate Report \n"
                   "5.Exit"))
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
                    self.running = False
                case _:
                    print("Invalid input")

if __name__ == "__main__":
    ft = FinanceTracker()
    ft.main_menu() 
