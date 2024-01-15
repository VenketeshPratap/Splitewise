# app/services.py
from flask_mail import Message
from app import mail
from app.models import User 
from pymongo import MongoClient
class ExpenseService:
    def __init__(self):
        self.expenses = []
        self.client = MongoClient('mongodb+srv://venketeshmall2:BrZ5F7HXbvderjXQ@cluster0.agtpsff.mongodb.net/')
        self.db = self.client['splitwiseflask']
        self.expenses_collection = self.db['expenses']

    def add_user(self, user_id, name, email, mobile):
        user = User(user_id, name, email, mobile)
        self.users[name] = user

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.send_email_alert(expense)

    def send_email_alert(self, expense):
        # Implement email alert logic here
        for user in self.users.values():
            msg = Message('New Expense Alert', sender='your_email@example.com', recipients=[user.email])
            msg.body = f"Hello {user.name},\n\nA new expense has been added:\n\nAmount: {expense['amount']}\nPaid by: {expense['paid_by']}\n\nRegards,\nSplitwise App"
            mail.send(msg)

    def calculate_balances(self, users):
        balances = {user: {debtor: 0 for debtor in users} for user in users}

        for expense in self.expenses:
            amount = float(expense['amount'])
            paid_by = expense['paid_by']
            split_type = expense['split_type']
            split_values = expense['split_values']

            if split_type == 'EQUAL':
                # Handle equal splitting logic
                for user in users:
                    if user != paid_by:
                        balances[paid_by][user] += amount / (len(users) - 1)
                        balances[user][paid_by] -= amount / (len(users) - 1)

            elif split_type == 'EXACT':
                # Handle exact splitting logic
                split_values = [float(val) for val in split_values.split(',')]
                for i, user in enumerate(users):
                    if user != paid_by:
                        balances[paid_by][user] += split_values[i]
                        balances[user][paid_by] -= split_values[i]

            elif split_type == 'PERCENT':
            # Handle percent splitting logic
                split_values = [float(val) for val in split_values.split(',')]
                for i, user in enumerate(users):
                    if user != paid_by:
                        balances[paid_by][user] += (amount * split_values[i] / 100)
                        balances[user][paid_by] -= (amount * split_values[i] / 100)

    # Filter out users with zero balance or negative balance
        filtered_balances = {user: {debtor: amount for debtor, amount in user_balances.items() if amount > 0} for user, user_balances in balances.items() if any(amount > 0 for amount in user_balances.values())}

        return filtered_balances

    