import requests
from bs4 import BeautifulSoup

budget = []
name = []

for i in range(57):
    url = 'https://www.the-numbers.com/movie/budgets/all/' + str(100*i + 1)
    result = requests.get(url)
    c = result.content
    soup = BeautifulSoup(c, features = "lxml")
    samples = soup.find_all("td", class_= "data")
    names = soup.find_all("table")

    for i, c in enumerate(samples):
        if i % 4 == 1:
            budget.append(c.contents)

    for n in names[0].find_all('b'):
        name.append(n.a.contents)

with open('budgets.txt', 'w') as f:
    for i in range(len(budget)):
        res = str(name[i]) + " " + str(budget[i]) + "\n"
        f.write(res)
f.close()

