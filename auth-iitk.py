import urllib.request
import time
import urllib.parse
from bs4 import BeautifulSoup as Soup

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')]

username = 'Put your username here'
password = 'Put your password here'

check = True
while check:
    try:
        test = opener.open('https://gateway.iitk.ac.in:1003/login?a7ae5f3cc31d8')
        print("Connecting...")
        check = False
    except:
        time.sleep(2)
        print("Trying to connect to https://gateway.iitk.ac.in:1003")

html = test.read()
parsed = Soup(html, 'html.parser')

data = {"4Tredir": "https://gateway.iitk.ac.in:1003/login?a7ae5f3cc31d8", "username": username, "password": password}
form = parsed.findAll('form')[0]
magic = form.findAll('input')[1]['value']
data['magic'] = str(magic)

time.sleep(2)
login_data = urllib.parse.urlencode(data).encode('utf-8')
try:
    test = opener.open('https://gateway.iitk.ac.in:1003', login_data)
    print('Connection established')
except:
    print('Cannot connect now')

html = test.read()

parsed = Soup(html, 'html.parser')
script_tag = parsed.find('script', {'language': 'JavaScript'})
script_content = script_tag.string
key = script_content.split('?')[1][:-2]
url = 'https://gateway.iitk.ac.in:1003/keepalive?' + key
# time.sleep(2400)
time.sleep(2350)

while True:
    try:
        opener.open(url)
        print('Authentication refreshed... ')
        time.sleep(2350)
    except:
        print('Cannot refresh the authentication ', url)
        time.sleep(10)







