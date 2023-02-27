from pymongo import MongoClient
from bs4 import BeautifulSoup

client = MongoClient('mongodb://localhost:27017/')
db = client.framework_test
col = db.framework
with open("/html/pytest_report.html") as file:
    soup = BeautifulSoup(file, 'html.parser')

table = soup.find('table', id="results-table")
tbody = table.find_all('tbody')

results = []
for t in tbody:
    tr = t.find('tr')
    td_list = tr.find_all('td')
    result = {'result': td_list[0].text.strip(), 'name': td_list[1].text.strip(),
              'duration': float(td_list[2].text.strip()),
              'links': td_list[3].text.strip()}
    results.append(result)
col.insert_one({'tests': results})

print(results)

# col[td_list[1].text.strip().split("::")[1]].insert_one(result)
