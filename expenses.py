def category_summary(expenses):
    summary={}
    for expense in expenses:
        category=expense["Category"]
        amount=expense["Amount"]
        
        if category in summary:
            summary[category]=summary.get(category)+amount
        else:
            summary[category]=amount
    return summary

def add_expense(expenses):
    expense={}
    try:
        Amount=int(input("Enter expense amount:"))
    except ValueError:
        print("Enter a valid amount:")
        return None
    category=input("Enter category:")
    Description=input("Enter description of expense:")
    expense["Amount"]=Amount
    expense["Category"]=category
    expense["Description"]=Description
    expenses.append(expense)
    return Amount