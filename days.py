days=int(input("enter the no of days="))
year=days//356
re_days=days%365             #re_months-remaning days in months
print("no of years are=",year)
months=re_days//30
re_months=re_days%30
print("no of months are=",months)
weeks=re_months//7
re_week=re_months%7
print("no of weeks are =",weeks)
day=re_week//1
print("no of days=",day)