from datetime import datetime

def check_expiry(expiry_date):
    """
    Returns (days_left, status)
    Status: SAFE, NEAR, URGENT
    """
    today = datetime.today()
    expiry = datetime.strptime(expiry_date, "%Y-%m-%d")
    print(expiry_date)
    days_left = (expiry - today).days

    if days_left <= 3:
        return days_left, "URGENT"
    elif days_left <= 7:
        return days_left, "NEAR"
    else:
        return days_left, "SAFE"
