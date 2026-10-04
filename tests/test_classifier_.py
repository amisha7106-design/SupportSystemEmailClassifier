from src.classifier import classify_email


def test_critical_email():
    assert classify_email("System is down") == "CRITICAL"


def test_high_email():
    assert classify_email("Payment failed") == "HIGH"


def test_medium_email():
    assert classify_email("I have a problem") == "MEDIUM"


def test_low_email():
    assert classify_email("I need some information") == "LOW"