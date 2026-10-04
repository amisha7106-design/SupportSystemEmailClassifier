from typing import Literal
from src.preprocessing import preprocess_email

Severity = Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]


def classify_email(email: str) -> Severity:
    """Classify a support email based on keywords."""

    email = preprocess_email(email).lower()

    if any(word in email for word in [
        "critical",
        "system down",
        "data loss",
        "production down",
        "complete outage"
    ]):
        return "CRITICAL"

    if any(word in email for word in [
        "urgent",
        "payment failed",
        "security issue",
        "unable to login",
        "account blocked"
    ]):
        return "HIGH"

    if any(word in email for word in [
        "problem",
        "issue",
        "error",
        "refund",
        "not working"
    ]):
        return "MEDIUM"

    return "LOW"