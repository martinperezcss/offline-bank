# Offline Wallet Manager 🪙

A lightweight, console-based Python application for managing multiple wallets using the [`pandas`](https://pandas.pydata.org/) library.

---

## 🧠 Context

This project was developed during a major power outage, with **no internet, no documentation, and no AI tools**.  
Armed only with a local code editor, a working Python environment, and my existing knowledge, I built this wallet management system in approximately 2 hours.  

The application demonstrates how to approach a technical challenge with limited resources and includes the following features:

- **Wallet Management**: Add new wallets, deposit, or withdraw funds.
- **Interest Calculations**: Compute simple and compound interest for wallet balances.
- **Statistical Summaries**: Calculate the total, average, highest, and lowest wallet balances.
- **CSV Integration**: Reads wallet data from a CSV file (`db.csv`).

This is not a production-ready solution but a quick offline exercise to showcase problem-solving under constraints.

---

## ▶️ How to Run

1. **Install Dependencies**  
   Ensure you have Python installed, then install the required library:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**  
   Execute the script in your terminal:

   ```bash
   python main.py
   ```

3. **Interact with the Menu**  
   Use the interactive menu to perform operations on the wallets. The initial data in [`db.csv`](db.csv) looks like this:

   ```csv
   name,balance
   "wallet1",3
   "wallet2",2
   ```

---

## 🛠️ Features

- **Add to Wallet**: Deposit funds into an existing wallet.
- **Withdraw from Wallet**: Withdraw funds from an existing wallet.
- **Create New Wallet**: Add a new wallet with a starting balance of 0.
- **Calculate Statistics**:
  - Total balance across all wallets.
  - Average balance across all wallets.
  - Wallet with the highest balance.
  - Wallet with the lowest balance.
- **Interest Calculations**:
  - Simple interest.
  - Compound interest.
- **Reset Wallet**: Wipe a wallet's balance to 0.

---

## 🚧 Known Limitations

- **No Persistence**: Changes made during runtime are not saved back to the [`db.csv`](db.csv) file.
- **No Input Validation**: The program assumes valid inputs and may crash with invalid data.
- **Index Handling**: Manually editing the CSV file may cause index-related issues.
- **Basic Error Handling**: Limited error handling is implemented.

---

## ✍️ Final Thoughts

This project is a snapshot of how to solve problems when modern tools are unavailable.  
Sometimes, programming is just you, a blank screen, and what you remember — and that can be enough to build something functional.  

Feel free to improve or expand upon this project as you see fit!

---