from datetime import datetime


def know_date():
    date = datetime.now().strftime("%d/%m/%Y, %H:%M")
    return date

def date_validator(date):
    try:
        datetime.strptime(date, "%d/%m/%Y")
        return True
    except ValueError:
        return False
    
def is_future_date(date):
    try:
        date = datetime.strptime(date, "%d/%m/%Y")
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return date >= today
    except ValueError:
        return False

