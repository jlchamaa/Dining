from  bs4 import BeautifulSoup
import urllib2

def tagstripper(soupObject,tagType):
    return soupObject.find(tagType).get_text().strip()

def no_dash(time):
    return time.split()[0]

def getinfo():
    url = "https://secure5.ha.ucla.edu/restauranthours/dining-hall-hours-by-day.cfm"
    response = urllib2.urlopen(url)
    html_doc = response.read()
    soup=BeautifulSoup(html_doc)
    first_find=soup.find("table",{"border":1})
    info=first_find.findAll('tr')
    #info holds all of the tr's (rows of information)
    return info
def mktimedict(info,row):
    restaurant=info[row].findAll('strong')
    for tag in restaurant:
        print no_dash(tag.get_text().strip())
    
    
    
    
         
def main():
    info=getinfo()
    mktimedict(info,5)



if __name__=="__main__":
    main()      
