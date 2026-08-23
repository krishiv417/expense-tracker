import csv
def save_expenses(expenses):
    with open("data/expenses.csv","w",newline="") as file:
        fieldnames=["Amount","Category","Description"]
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def load_expenses():
    expenses=[]
    try:
        with open("data/expenses.csv","r",newline="") as file:
            reader=csv.DictReader(file)
            for row in reader:
                row["Amount"]=int(row["Amount"])
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses