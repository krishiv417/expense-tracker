import matplotlib.pyplot as plt
from expenses import category_summary
def show_category_chart(expenses):
    summary=category_summary(expenses)
    categories=summary.keys()
    amounts=summary.values()

    plt.bar(categories,amounts)
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.title("Spending by category")
    plt.show()