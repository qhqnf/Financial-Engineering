# %%
import requests
from bs4 import BeautifulSoup
import numpy as np
import QuantLib as ql

maturity_list = []
yield_list = []

# %%
# getting data

with requests.get("https://tradingeconomics.com/united-states/repo-rate") as request:
    soup = BeautifulSoup(request.text, "html.parser")
    repo_table = soup.find("table")
    repo_actual = repo_table.find_all("tr")[1].find_all("td")[1].get_text()
    maturity_list.append("O/N")
    yield_list.append(float(repo_actual))

# %%
request = requests.get(
    "https://tradingeconomics.com/united-states/government-bond-yield")
soup = BeautifulSoup(request.text, "html.parser")
bond_table = soup.find("table").find_all("tr")
for row_items in bond_table[1:]:
    maturity = row_items.find_all("td")[0].get_text(strip=True)
    y = row_items.find_all("td")[1].get_text(strip=True)
    maturity_list.append(maturity)
    yield_list.append(float(y))


temp = maturity_list[1]
maturity_list.remove(maturity_list[1])
maturity_list.append(temp)


# making date array
start_date = ql.Date_todaysDate()
print(f"Today is {start_date}")

period_array = np.array([ql.Period(1, ql.Days), ql.Period(1, ql.Months), ql.Period(3, ql.Months),
                         ql.Period(6, ql.Months), ql.Period(52, ql.Weeks), ql.Period(
    2, ql.Years), ql.Period(3, ql.Years), ql.Period(5, ql.Years),
    ql.Period(7, ql.Years), ql.Period(10, ql.Years), ql.Period(20, ql.Years), ql.Period(30, ql.Years)])


# build calender
maturity_date = []

us_cal = ql.UnitedStates()
for period in period_array:
    modified_date = us_cal.advance(
        start_date, period, ql.ModifiedFollowing, True)
    maturity_date.append(modified_date)

maturity_date_array = np.array(maturity_date)
print(maturity_date_array)


# concatenate arrays
maturity_array = np.array(maturity_list)
yield_array = np.array(yield_list)

bond = np.column_stack((maturity_array.T, yield_array.T,
                        maturity_date_array.T))

print(bond)
