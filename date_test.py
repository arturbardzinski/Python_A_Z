from datetime import datetime

def date_now():
    now = datetime.now()
    return now.strftime('%Y')

x = date_now()
print(x)
