from bs4 import BeautifulSoup
import requests


req = requests.get('https://www.365chess.com/eco.php')

soup = BeautifulSoup(req.content, 'html.parser')

table = soup.find_all('div', class_ = 'opname' )

chessOpenings = [i.getText() for i in table]

print(len(chessOpenings))