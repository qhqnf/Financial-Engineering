import numpy as np
import QuantLib as ql

start_date = ql.Date_todaysDate()
print(f"Today is {start_date}")

period_array = np.array([ql.Period(1, ql.Days), ql.Period(1, ql.Months), ql.Period(3, ql.Months),
                         ql.Period(6, ql.Months), ql.Period(52, ql.Weeks), ql.Period(
    2, ql.Years), ql.Period(3, ql.Years), ql.Period(5, ql.Years),
    ql.Period(7, ql.Years), ql.Period(7, ql.Years), ql.Period(10, ql.Years), ql.Period(20, ql.Years), ql.Period(30, ql.Years)])

maturity_date = start_date + period_array

print(maturity_date)
