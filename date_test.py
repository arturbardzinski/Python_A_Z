from datetime import datetime

def date_now():
    now = datetime.now()
    print(now.year)

date_now()