import requests
from io import StringIO

r=requests.get('http://202.204.105.22/academic/getCaptcha.do')
def getCpatcha():
    f=open('//static//c.jpg',mode='wb')
    f.write(r.content)
    f.close()



