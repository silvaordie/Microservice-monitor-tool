from Service import Service
import requests
from bs4 import BeautifulSoup

class BitBucket(Service):

    def __init__(self, url):
        Service.__init__(self, "bitbucket", "BitBucket", url)

    def getStatus(self, update):
        if update:
            try:
                r = requests.get(self.url)
                try:
                    soup = BeautifulSoup(r.text, 'html.parser')

                    results = soup.find_all('span', attrs={'class':'status font-large'})

                    self.status = " ".join(results[0].contents[0].split())
                except:
                    self.status = "Uknown HTML configuration"
            except:
                self.status = "Unable to reach server"

        return self.status