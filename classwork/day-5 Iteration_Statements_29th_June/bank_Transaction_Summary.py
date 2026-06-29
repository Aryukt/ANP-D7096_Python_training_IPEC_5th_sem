'''Bank Transaction Summary
Problem Statement
A customer keeps entering transaction amounts.
Positive numbers indicate deposits, while negative numbers indicate withdrawals.
The customer enters 0 to finish.
Display:
• Total Deposit
• Total Withdrawal
• Final Balance'''
total_deposit = 0
total_withdrawal = 0
while True:
    transaction = float(input("Enter transaction amount (0 to finish): "))
    if transaction == 0:
        break
    elif transaction > 0:
        total_deposit += transaction
    else:
        total_withdrawal += abs(transaction)
        
final_balance = total_deposit - total_withdrawal

print(f"Total Deposit: {total_deposit}")
print(f"Total Withdrawal: {total_withdrawal}")
print(f"Final Balance: {final_balance}")
