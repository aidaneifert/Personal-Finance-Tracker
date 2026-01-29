import json

class FinanceTracker():

    def __init__(self):
        self.entries= []

        try:
            with open('Data.json', 'r') as f: 
                self.entries = json.load(f)

        except FileNotFoundError:
            print("WARNING: json storage file does not exist,"
                  " a new blank json was made.")
            with open("Data.json", "w") as f:
                json.dump([], f, indent= 4)
                
    def user_input(self):
        i = input(">")
        return i.strip()

    def save_to_file(self):
        with open('Data.json', 'w') as f:
            json.dump(self.entries, f, indent= 4)

    def add_income(self):       #work to do
        id = [d["id"] for d in self.entries]

        if not id:
            new_id = 1
        else:
            i= len(self.entries)
            new_id= i + 1

        while True:
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

            empty_counter= [key for key, value in new_input.items() if value == ""]

            if empty_counter:
                for key in empty_counter:
                    if key == "amount":
                        print(f"you did not add an {key}")
                    else:
                        print(f"you did not add a {key}")
                continue
            
            elif not empty_counter:
                self.entries.append(new_input)
                self.save_to_file()
                break
            
        # try to make it remember entered values and only ask for ones not provided

    def add_expense(self):      #work to do
        id = [d["id"] for d in self.entries]

        if not id:
            new_id = 1
        else:
            i= len(self.entries)
            new_id= i + 1
            
        while True:
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

            empty_counter= [key for key, value in new_input.items() if value == ""]

            if empty_counter:
                for key in empty_counter:
                    if key == "amount":
                        print(f"you did not add an {key}")
                    else:
                        print(f"you did not add a {key}")
                continue

            elif not empty_counter:
                self.entries.append(new_input)
                self.save_to_file()
                break

        # try to make it remember entered values and only ask for ones not provided

    def show_entries(self):
        if not self.entries:
            print("You have no entries")
        else:
            for dicts in self.entries:
                for key,transacts in dicts.items():
                    print(f"{key}:{transacts}")
            while True:
                print("\ntype e to edit, type r to remove, press enter to exit")
                i = self.user_input().lower()

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
        expenses= [d for d in self.entries if d.get("type") == "expense"]
        income= [d for d in self.entries if d.get("type") == "income"]
        total_income= 0
        total_expenses= 0

        for i in income:
            for key, value in i.items():
                if key == "amount":
                    total_income=  total_income + int(value) 

        for e in expenses:
            for key, value in e.items():
                if key == "amount":
                    total_expenses= total_expenses + int(value)

        remaining_money= total_income - total_expenses
        print(f"You have made {total_income} \nYou have spent {total_expenses} \nYou have {remaining_money} remaining")
        input("Press Enter to continue")
     
    def edit_entry(self):
        print("Enter a transaction id to edit") 
        user_input= self.user_input()

        try:
            to_remove = int(user_input)
        except ValueError:
            print("Invalid Input")

        if to_remove > len(self.entries):
            print("the id you entered does not exist")
            return
        
        elif to_remove <= 0:
            print("the id you entered does not exist")
            return
        
        for i, d in enumerate(self.entries):
            if d.get("id") == to_remove:
                entry= self.entries.pop(i)

        dict_id= entry.get("id")
        dict_type= entry.get("type")

        match dict_type:
            case "expense":
                while True:
                    amount= entry.get("amount")
                    category= entry.get("category")
                    date= entry.get("date")
                    description= entry.get("description")

                    new_amount= input(f"Previous value: {amount} >")
                    new_category= input(f"Previous value: {category} >")
                    new_date= input(f"Previous value: {date} >")
                    new_description= input(f"Previous value: {description} >")

                    new_input= {
                    "id":dict_id,
                    "type":dict_type,
                    "amount":new_amount, 
                    "category":new_category,
                    "date":new_date, 
                    "description":new_description
                    }
                    empty_counter= [key for key, value in new_input.items() if value == ""]

                    if empty_counter:
                        for key in empty_counter:
                            if key == "amount":
                                print(f"you did not add an {key}")
                            else:
                                print(f"you did not add a {key}")
                        continue

                    elif not empty_counter:
                        self.entries.append(new_input)
                        self.save_to_file()
                        break    

            case "income":
                while True:
                    amount= entry.get("amount")
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

                    empty_counter= [key for key, value in new_input.items() if value == ""]

                    if empty_counter:
                        for key in empty_counter:
                            if key == "amount":
                                print(f"you did not add an {key}")
                            else:
                                print(f"you did not add a {key}")
                        continue

                    elif not empty_counter:
                        self.entries.append(new_input)
                        self.save_to_file()
                        break                
 
    def remove_entry(self):
        new_id= 1
        print("Enter a transaction id to remove") 

        try:
            to_remove = int(self.user_input())

        except ValueError:
            print("Invalid input")

        if to_remove > len(self.entries):
            print("the id you entered does not exist")
            return

        elif to_remove <= 0:
            print("the id you entered does not exist")
            return
        
        for i, d in enumerate(self.entries):
            if d.get("id") == to_remove:
                self.entries.pop(i)

        for d in self.entries:
            d["id"]= new_id
            new_id= new_id + 1
            
        self.save_to_file()

    def main_menu(self):
        while True:

            print(("1.Add Income \n"
                   "2.Add Expense \n"
                   "3.Show/Edit Entries \n"
                   "4.Generate Report \n"
                   "5.Exit"))
            user_input= self.user_input() 

            match user_input:          
                case "1":
                    self.add_income()
                case "2":
                    self.add_expense()
                case "3":
                    self.show_entries()
                case "4":
                    self.generate_report()
                case "5":
                    break
                case _:
                    print("Invalid input")

if __name__ == "__main__":
    ft = FinanceTracker()
    ft.main_menu() 
