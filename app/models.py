class User:
    def __init__(self, user_id, name, email, mobile):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile = mobile


class Expense:
    def __init__(self, expense_id, amount, paid_by, splits, metadata):
        self.expense_id = expense_id
        self.amount = amount
        self.paid_by = paid_by
        self.splits = splits
        self.metadata = metadata
