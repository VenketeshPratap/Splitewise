
from flask import render_template, request, jsonify
from app import app
from app.services import ExpenseService
# Dummy data, replace with actual data retrieval logic
users = ["User1", "User2", "User3", "User4"]

expense_service = ExpenseService()  # Create an instance of ExpenseService

@app.route('/')
def index():
    return render_template('index.html', users=users)


@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        # Assuming the user information is sent as JSON in the request body
        user_data = request.json

        user_id = f"u{len(expense_service.users) + 1}"  # Incremental user_id
        name = user_data.get('name')
        phone_number = user_data.get('phone_number')
        email = user_data.get('email')

        # Validate required fields
        if not name or not phone_number or not email:
            return jsonify({"error": "Invalid user data. Please provide all required fields."}), 400

        # Add the user using the ExpenseService
        expense_service.add_user(user_id, name, phone_number, email)

        return jsonify({"message": "User added successfully."})

    except Exception as e:
        return jsonify({"error": f"Error adding user: {str(e)}"}), 500

@app.route('/add_expense', methods=['POST'])
def add_expense():
    amount = request.form.get('amount')
    paid_by = request.form.get('paidBy')
    split_type = request.form.get('splitType')
    split_values = request.form.get('splitValues', '')

    expense_data = {
        'amount': amount,
        'paid_by': paid_by,
        'split_type': split_type,
        'split_values': split_values,
    }

    expense_service.expenses.append(expense_data)

    return jsonify({'message': 'Expense added successfully'})


# Other routes and logic...
@app.route('/show_balances')
def show_balances():
    users = ["User1", "User2", "User3", "User4"]
    balances = expense_service.calculate_balances(users)

    return jsonify(balances)