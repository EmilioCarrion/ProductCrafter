from main import process_payment

def test_valid_credit_card_payment(capsys):
    assert process_payment(500.0, "user123", "CreditCard") is True
    captured = capsys.readouterr()
    assert "Processing credit card payment for user user123" in captured.out

def test_valid_paypal_payment(capsys):
    assert process_payment(500.0, "user123", "PayPal") is True
    captured = capsys.readouterr()
    assert "Processing PayPal payment for user user123" in captured.out

def test_invalid_payment_amount(capsys):
    assert process_payment(-100.0, "user123", "CreditCard") is False
    captured = capsys.readouterr()
    assert "Invalid payment amount: -100.0 for user user123" in captured.out

def test_invalid_user_id(capsys):
    assert process_payment(500.0, "u", "CreditCard") is False
    captured = capsys.readouterr()
    assert "Invalid userId: u" in captured.out

def test_invalid_payment_method(capsys):
    assert process_payment(500.0, "user123", "InvalidMethod") is False
    captured = capsys.readouterr()
    assert "Invalid payment method: InvalidMethod" in captured.out