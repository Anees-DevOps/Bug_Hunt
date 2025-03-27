def withdraw(amount, balance):
    if amount > balance:
        raise ValueError("Insufficient funds!")  # ✅ Prevents negative balance
    return balance - amount
