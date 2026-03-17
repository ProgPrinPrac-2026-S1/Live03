def interest(principal, rate):
    amount = principal * (1 + rate)
    return amount

for rate in range(1, 10):
    principal = 500
    amount = interest(principal, rate/100.0)
    print(f"Principal: ${principal:.2f}  Rate: {rate}%  Amount: ${amount:.2f}")
