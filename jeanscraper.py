from  bs4 import BeautifulSoup
import urllib2

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
    hourlist=[]
    for tag in restaurant:
        hourlist.append(no_dash(tag.get_text().strip()))
    return hourlist

def main():
    info=getinfo()
    diction={}
#    for rstr in range(12):  #where 12 is # of restuarants
#        diction[rstr,mktimedict(info,rstr)]
    print mktimedict(info,4)
    print restaurant    


if __name__=="__main__":
    main()      
