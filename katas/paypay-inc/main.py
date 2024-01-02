def process_payment(amount, user_id, payment_method):
    if amount > 0 and len(user_id) >= 3:
        if payment_method == "CreditCard":
            # Simulate credit card payment processing
            print(f"Processing credit card payment for user {user_id}")
            # Additional logic...
            return True  # Assuming successful payment
        elif payment_method == "PayPal":
            # Simulate PayPal payment processing
            print(f"Processing PayPal payment for user {user_id}")
            # Additional logic...
            return True  # Assuming successful payment
        else:
            print(f"Invalid payment method: {payment_method}")
    else:
        if amount <= 0:
            print(f"Invalid payment amount: {amount} for user {user_id}")
        if len(user_id) < 3:
            print(f"Invalid userId: {user_id}")
    return False