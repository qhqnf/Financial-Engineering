# %%
import requests
from bs4 import BeautifulSoup

# %%
with requests.get("https://tradingeconomics.com/united-states/repo-rate") as request:
    soup = BeautifulSoup(request.text, "html.parser")
    repo_table = soup.find("table")
    repo_actual = table.find_all("tr")[1].find_all("td")[1].get_text()
    print(repo_actual)

# %%
request = requests.get(
    "https://tradingeconomics.com/united-states/government-bond-yield")
soup = BeautifulSoup(request.text, "html.parser")
bond_table = soup.find("table").find_all("tr")
bonds = []
for row_items in bond_table[1:]:
    maturity = row_items.find_all("td")[0].get_text(strip=True)
    y = row_items.find_all("td")[1].get_text(strip=True)
    obj = {
        "maturity": maturity,
        "yield": y
    }
    bonds.append(obj)
print(bonds)


# %%
