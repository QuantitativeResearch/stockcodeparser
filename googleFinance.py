from urllib.request import urlopen
import json
import time

class GoogleFinanceAPI:
    def __init__(self):
        self.prefix = "http://finance.google.com/finance/info?client=ig&q="
    
    def get(self,symbol,exchange):
        url = self.prefix+"%s:%s"%(exchange,symbol)
        u = urlopen(url)
        content = u.read().decode('cp1252')
        
        obj = json.loads(content[3:])
        return obj[0]
        
        
if __name__ == "__main__":
    c = GoogleFinanceAPI()
    
    while 1:
        quote = c.get("XIN9","INDEXFTSE")
        print (quote)
        time.sleep(5)