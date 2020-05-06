import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://database.lichess.org/'
req = requests.get(url)


soup = BeautifulSoup(req.content, 'html.parser')

tableContent = soup.select_one('table')
output_rows = []
for table_row in tableContent.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)

df = pd.DataFrame(output_rows, columns=['Month', 'Size', 'Games', 'Clock', 'File'])
# Drop the first row
df.drop(df.index[:1], inplace=True)
# Drop the last row
df.drop(df.index[-1:], inplace=True)
# Change the , to nothing and We can use it as a number
df.Games = df.Games.str.replace(',', '').astype(int)
print(df.Games.sum())