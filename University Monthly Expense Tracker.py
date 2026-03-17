expenses = []

def add_expense(amount, category):
    expenses.append({'amount': amount, 'category': category})

def total_by_category(cat):
    return sum(item['amount'] for item in expenses if item['category'] == cat)

def show_all_expenses():
    for item in expenses:
        print(f"{item['category']}: {item['amount']} Birr")

add_expense(3000, 'Food')
add_expense(60, 'Dorm')
add_expense(120, 'Course Materials')

print("University Monthly Cost-Sharing Expenses:")
show_all_expenses()

total = sum(item['amount'] for item in expenses)
print("\nTotal Monthly Expenses:", total, "Birr")
