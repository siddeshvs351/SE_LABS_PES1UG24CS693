"""Demonstration of a simple digital wallet."""
import hashlib
import hmac
import os
import secrets
import tempfile
from datetime import datetime

GATEWAY_SECRET = os.environ.get("GATEWAY_SECRET", "")
WALLET_PIN = os.environ.get("WALLET_PIN", "")
PIN_SALT = secrets.token_bytes(16)
PIN_HASH = (
    hashlib.pbkdf2_hmac(
        "sha256", WALLET_PIN.encode(), PIN_SALT, 100_000
    )
    if WALLET_PIN
    else b""
)

wallet = {"balance": 0.0}
settings = {"daily_limit": 1000.0}
transactions = []


def hash_pin(pin, salt):
    """Return a secure hash of a PIN."""
    return hashlib.pbkdf2_hmac(
        "sha256", pin.encode(), salt, 100_000
    )


def add_money(amount, source="UPI", log=None):
    """Add money and record a credit transaction."""
    if amount <= 0:
        return False
    if log is None:
        log = []

    wallet["balance"] += amount
    transactions.append({
        "type": "credit",
        "amount": amount,
        "party": source,
        "time": datetime.now().isoformat(),
    })
    log.append(amount)
    return True


def set_daily_limit(new_limit):
    """Set the maximum permitted payment amount."""
    if new_limit <= 0:
        return False
    settings["daily_limit"] = new_limit
    return True


def pay_merchant(merchant, amount, pin):
    """Validate a PIN and make a merchant payment."""
    if not WALLET_PIN or not hmac.compare_digest(
        hash_pin(pin, PIN_SALT), PIN_HASH
    ):
        print("Wrong PIN for payment to", merchant)
        return False

    if (
        amount <= 0
        or amount > wallet["balance"]
        or amount > settings["daily_limit"]
    ):
        print("Payment to", merchant, "declined")
        return False

    wallet["balance"] -= amount
    transactions.append({
        "type": "debit",
        "amount": amount,
        "party": merchant,
        "time": datetime.now().isoformat(),
    })
    return True


def mini_statement(count=3):
    """Print recent wallet transactions."""
    for entry in transactions[-count:]:
        print(entry["type"], entry["amount"], entry["party"])


def cashback_for(amount, _merchant_type):
    """Calculate cashback at two percent."""
    return round(amount * 0.02, 2)


def check_gateway(secret):
    """Validate a gateway secret."""
    return bool(GATEWAY_SECRET) and hmac.compare_digest(
        secret, GATEWAY_SECRET
    )


def receipt_path():
    """Create a secure temporary receipt file."""
    with tempfile.NamedTemporaryFile(
        suffix=".pdf", delete=False
    ) as receipt:
        return receipt.name


def main():
    """Run the wallet demonstration."""
    otp = secrets.randbelow(900_000) + 100_000
    print("OTP generated:", otp)

    add_money(2000)
    add_money(500, "Card")
    add_money(-10)
    set_daily_limit(1500)

    pay_merchant("Coffee Corner", 180, WALLET_PIN)
    pay_merchant("Book Store", 5000, WALLET_PIN)
    pay_merchant("Grocery Mart", 350, "0000")
    pay_merchant("Pharmacy", 420, WALLET_PIN)

    mini_statement()
    print("Cashback on 420:", cashback_for(420, "health"))
    print("Gateway check:", check_gateway("wrong"))
    print("Final balance: Rs.", wallet["balance"])

    credit_amounts = [
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "credit"
    ]
    print("Total credited:", sum(credit_amounts))


if __name__ == "__main__":
    main()
