# Bank Management System 🏦

This is a graphical desktop application for managing bank accounts, built using Python and the Tkinter library. The system allows users to perform essential banking operations such as opening an account, depositing funds, and withdrawing money. The project integrates a MySQL database to securely store user information and account balances.

---

## Features ✨

- **Open Account**: Users can create new accounts by entering their username and password.
- **Deposit Money**: Users can deposit funds into their account by providing their username and the amount.
- **Withdraw Money**: Users can withdraw funds after entering their username, password, and amount (if sufficient balance exists).
- **Validation**: Ensures secure operations with password checks and error handling for invalid inputs.
- **Responsive Design**: Adapts to the screen size for better usability.

---

## Technologies Used 💻

- **Frontend**: Python (Tkinter for GUI)
- **Backend**: MySQL (pymysql for database integration)

---

## Setup Instructions ⚙️

1. **Install Required Libraries**:
   - Install Python (v3.7 or above).
   - Install MySQL and ensure it's running on your system.
   - Install the `pymysql` library using the command:
     ```bash
     pip install pymysql
     ```

2. **Database Configuration**:
   - Create a MySQL database named `bankdb`.
   - Create a table named `account` with the following structure:
     ```sql
     CREATE TABLE account (
         userName VARCHAR(255) PRIMARY KEY,
         userPW VARCHAR(255),
         balance INT DEFAULT 0
     );
     ```

3. **Run the Application**:
   - Clone this repository:
     ```bash
     git clone https://github.com/your-username/bank-management-system.git
     cd bank-management-system
     ```
   - Execute the script:
     ```bash
     python bank_management_system.py
     ```

---

## How It Works 🔧

1. **Launch the Application**:
   - The main screen presents options for managing accounts.

2. **Open an Account**:
   - Enter a username and password to create an account.

3. **Deposit Money**:
   - Enter your username and deposit amount to add funds to your account.

4. **Withdraw Money**:
   - Enter your username, password, and the withdrawal amount (ensuring sufficient balance).

5. **Validation and Security**:
   - Passwords are validated during account operations.
   - Alerts are displayed for invalid inputs or operations.

---

## Screenshots 🖼️

![image alt](https://github.com/bhuvaneswarreddy123/Bank-Account-Management-System/blob/main/images/BankDetails.png?raw=true)


---

## Future Enhancements 🚀

- Add a transaction history feature.
- Implement account deletion and update functionality.
- Add encryption for secure password storage.
- Create a user-friendly installer for ease of use.

---

## License 📜

This project is open-source and available under the [MIT License](LICENSE).
