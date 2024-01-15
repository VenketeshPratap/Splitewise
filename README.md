# Splitewise
An expense sharing application is where you can add your expenses and split it among different people. The app keeps balances between people as in who owes how much to whom.

# Splitwise Application
## Overview
This is a simple expense-splitting application built with Flask and MongoDB. The application allows users to add expenses, track balances, and receive email alerts for new expenses.

## Features
- **Add Expense:** Users can add new expenses, specifying the amount, paid by, and split details.
- **Show Balances:** View a balance sheet to see how much each user owes or is owed by others.
- **User Management:** Add new users to the system with unique user IDs, names, email addresses, and phone numbers. 
- **Email Alerts:** Receive email alerts when a new expense is added.

## Architecture
The application follows a client-server architecture:
- **Frontend:** HTML, CSS, and JavaScript.
- **Backend:** Flask for the server and handling API requests.
- **Database:** MongoDB Atlas for storing user information and expenses.
- **Email Notifications:** Integrates with a service for sending email alerts.
  
Install dependencies:
Run the application:
python run.py
API Endpoints
POST /add_user: Add a new user to the system.
POST /add_expense: Add a new expense.
GET /show_balances: View the balance sheet.

Database Schema
The MongoDB database has two collections:

users:
user_id
name
email
phone_number

expenses:
amount
paid_by
split_type
split_values
