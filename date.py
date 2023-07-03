from datetime import datetime
import pandas as pd
from datetime import date
from dateutil import relativedelta

def age_left():
    x= input("Enter your date of birth: ")
    x= datetime.strptime(x,"%d/%m/%Y").date()
    date_after_90 = pd.to_datetime(x)+pd.DateOffset(years = 90)
    #date_after_90 = datetime.strptime(date_after_90,"%d/%m/%Y").date()
    date_after_90 = date_after_90.strftime("%d/%m/%Y")
    date_after_90 = datetime.strptime(date_after_90, "%d/%m/%Y").date()
    print(f"date after 90days {date_after_90}")
    print(type(date_after_90))
    today = date.today()
    print(today)
    print(type(today))
    #d1=today.strftime("%d/%m/%Y")
    #d1 = datetime.strptime(today,"%d/%m/%Y").date()
    #print(type(d1))
    diff = relativedelta.relativedelta(date_after_90,today)
    print(diff.years, "years",diff.months, "Months",diff.days,"Days")

    #print(f"date today {d1}")

age_left()






