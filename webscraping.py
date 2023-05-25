import requests, bs4
# python -m pip install requests

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#should be 200
# res.status_code 
#check for if errors ok
#res.raise_for_status() 

#download text to file
#need to write in binary 

#playFile = open('RomeoAndJuliet.txt', 'wb')
#for chunk in res.iter_content(100000):
#    playFile.write(chunk)
#playFile.close()


#check upvotes
url = "https://weather.com/weather/tenday/l/89ab85d31edf7fc9099c46fc00397f4a760fffca2a71b2fecf56fbb3d8686dee"

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select('#detailIndex0 > div > div.DailyContent--DailyContent--1yRkH > div > div:nth-child(1) > span')
print(elems[0].text)
