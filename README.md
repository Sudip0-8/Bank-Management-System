# 🏦 Bank Management System

A simple Bank Management System built using Python that allows users to create and manage bank accounts through a command-line interface. The application uses JSON file handling to store and update customer information and account balances.

## 📌 Project Overview

The Bank Management System is designed to perform basic banking operations such as account creation, money deposit, withdrawal, viewing account details, updating customer information, and deleting accounts.

It uses Python's Object-Oriented Programming (OOP) concepts and JSON file handling to manage customer records and maintain account information.

## ✨ Features

- Create Bank Account: Register a new customer with their name, age, email, and PIN.
- Generate Account Number: Automatically generates a random account number containing letters, digits, and special characters.
- Deposit Money: Deposit money into an existing bank account.
- Withdraw Money: Withdraw money after verifying account credentials and checking the available balance.
- View Account Details: Display customer information after account verification.
- Update Account Details: Modify customer name, email address, and PIN.
- Delete Bank Account: Permanently remove an existing account after confirmation.
- JSON Data Storage: Store and update customer information using a JSON file.

## 🛠️ Technologies Used

- Programming Language: Python
- Data Storage: JSON
- Python Concepts:
  - Object-Oriented Programming (OOP)
  - Classes and Objects
  - Class Methods
  - Encapsulation
  - File Handling
  - Exception Handling
  - List Comprehensions
  - Random Number Generation

## 📂 Project Structure

```text
Bank-Management-System/
│
├── main.py        # Main Python application
├── data.json      # Stores customer and account information
└── README.md      # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Sudip0-8/Bank-Management-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Bank-Management-System
```

### 3. Run the Application

Make sure Python 3 is installed on your system.

```bash
python main.py
```

No external Python libraries are required. The project uses built-in Python modules.

## 🚀 How to Use

After running the application, a menu will appear with the following options:

| Option | Operation |
|---|---|
| 1 | Create a Bank Account |
| 2 | Deposit Money |
| 3 | Withdraw Money |
| 4 | View Account Details |
| 5 | Update Account Details |
| 6 | Delete Bank Account |

Select the desired option and follow the instructions displayed in the terminal.

## 💾 Data Management

The application uses a JSON file (`data.json`) to store customer records.

Each customer record contains:

- Name
- Age
- Email Address
- PIN
- Account Number
- Account Balance

Whenever an account is created, updated, deleted, or a transaction is performed, the changes are saved to the JSON file.

## 🔮 Future Improvements

- Implement a graphical user interface (GUI).
- Add transaction history and account statements.
- Improve input validation and error handling.
- Implement secure PIN storage and authentication.
- Add fund transfers between accounts.
- Integrate a database such as MySQL or PostgreSQL.

## 👨‍💻 Author

**Sudipto Baral**

GitHub: [@Sudip0-8](https://github.com/Sudip0-8)

---

⭐ If you find this project useful, consider giving the repository a star!
