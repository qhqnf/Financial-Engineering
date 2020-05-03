import numpy as np
import QuantLib as ql
import math

start_date = ql.Date_todaysDate()
print(f"Today is {start_date}")

"""
period_array = np.array([ql.Period(1, ql.Days), ql.Period(1, ql.Months), ql.Period(3, ql.Months),
                         ql.Period(6, ql.Months), ql.Period(52, ql.Weeks), ql.Period(
    2, ql.Years), ql.Period(3, ql.Years), ql.Period(5, ql.Years),
    ql.Period(7, ql.Years), ql.Period(7, ql.Years), ql.Period(10, ql.Years), ql.Period(20, ql.Years), ql.Period(30, ql.Years)])


# build calender
maturity_date = []

us_cal = ql.UnitedStates()
for period in period_array:
    modified_date = us_cal.advance(
        start_date, period, ql.ModifiedFollowing, True)
    maturity_date.append(modified_date)

maturity_date_array = np.array(maturity_date)
print(maturity_date_array)

modified_maturity = us_cal.advance(
    start_date, period_array, ql.ModifiedFollowing, True)

print(modified_maturity)
"""
pv = 1000000
r = 0.0326
days = 1

fv = pv*(1+r*days/360)
print(f"fv = {fv}")

dcf = 1/((1+r)**(days/360))
print(f"dcf = {dcf}")

zero_rate = math.log(1/dcf) / (5/365)
print(f"zero_rate = {zero_rate}")
