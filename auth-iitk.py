import urllib.request
import time
import urllib.parse

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')]

username = ''
password = ''

check = True
while check:
    try:
        test = opener.open('https://gateway.iitk.ac.in:1003/login?a7ae5f3cc31d8')
        print("Connecting...")
        check = False
    except:
        time.sleep(2)
        print("Trying to connect to https://gateway.iitk.ac.in:1003")

html = test.read().decode('utf-8')

# Extract the form action and magic value using string operations
form_start = html.find('<form')
form_end = html.find('</form>', form_start)
form_content = html[form_start:form_end]

magic_start = form_content.find('name="magic" value="') + len('name="magic" value="')
magic_end = form_content.find('"', magic_start)
magic = form_content[magic_start:magic_end]

data = {"4Tredir": "https://gateway.iitk.ac.in:1003/login?a7ae5f3cc31d8", "username": username, "password": password, "magic": magic}

time.sleep(2)
login_data = urllib.parse.urlencode(data).encode('utf-8')
try:
    test = opener.open('https://gateway.iitk.ac.in:1003', login_data)
    print('Connection established')
except:
    print('Cannot connect now')

html = test.read().decode('utf-8')

# Extract the keepalive URL using string operations
script_start = html.find('<script language="JavaScript">') + len('<script language="JavaScript">')
script_end = html.find('</script>', script_start)
script_content = html[script_start:script_end]

key_start = script_content.find('?') + 1
key_end = script_content.find("'", key_start)
key = script_content[key_start:key_end]
url = 'https://gateway.iitk.ac.in:1003/keepalive?' + key

time.sleep(2000)

while True:
    try:
        opener.open(url)
        print('Authentication refreshed... ')
        time.sleep(2000)
    except:
        print('Cannot refresh the authentication ', url)
        time.sleep(10)
