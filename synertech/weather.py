import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://apis.data.go.kr/1400377/forestPoint/forestPointListGeongugSearch?serviceKey=jPGoI0ScLmUHOHp7GaoEd0Xsbr0KF8LjyFOJkNr7DK8ypcQM6INJG7uh88WvsTfhqPJb5dLvwfqa0MYF9i3NHQ%3D%3D',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs =soup.select('body > items> item > analdate')

print(trs)
'''
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.synertech
'''

