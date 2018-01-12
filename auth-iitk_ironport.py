import urllib2, time, urllib

def internet_on():
    try:
        urllib2.urlopen('https://www.google.com', timeout=1)
        return False
    except urllib2.URLError as err:
        return True

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')]

username = 'Put your username here'
password = 'Put your password here'

data = {"username": username, "password":password, "sid":0}

login_data = urllib.urlencode(data)

while(True):

    check = internet_on()

    if check:
        try:
            test = opener.open('https://authenticate.iitk.ac.in/netaccess/loginuser.html', login_data)
            time.sleep(300)
        except:
            time.sleep(2)
            print 'Can not connect now'

    else:
        time.sleep(300)
