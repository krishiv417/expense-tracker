
from storage import save_expenses,load_expenses
from expenses import category_summary,add_expense
from report import show_category_chart



expenses=load_expenses()


total=0
for expense in expenses:
    total+=expense["Amount"]
while(True):
    print("1.ADD\n2.View\n3.Total_spent\n4.Category Summary\n5.Category Chart\n6.Exit")
    try:
        choice=int(input("Enter:"))
    except ValueError:
        print("Please enter a valid number")
        continue
    if choice==1:
       amount=add_expense(expenses)
       if amount is not None:
        total+=amount
    elif choice==2:
        print(expenses)
    elif choice==3:
        print("Total spent:",total)
    elif choice==4:
        print(category_summary(expenses))        
    elif choice==5:
        show_category_chart(expenses)
    elif choice==6:
        save_expenses(expenses)
        break
    else:
        print("Invalid choice!!")
