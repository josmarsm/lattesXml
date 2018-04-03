import urllib
import pandas as pd
from bs4 import BeautifulSoup

#http = urllib.PoolManager()

html_doc = urllib.urlopen('pgcc/Pj-0.html')
#response = http.request('GET', url)
soup = BeautifulSoup(html_doc,'html.parser')

soup.prettify()
#for anchor in soup.findAll('a', href=True):
 #   print anchor['href']

#table = soup.find('div', attrs={'class': 'content'})

rows = soup.findAll('tr')[2:]
#print ('impressao das linhas'+str(rows))
#print ('---------')
#for tr in rows:
for tr in soup.findAll('tr')[2:]:
    cols = tr.findAll('td')
    #campo1 = cols[1].text.split(".",1)
    #ordem,digital_code  = [c.text for c in cols]
    print "Campo1: %s, Campo2: %s, Campo3: %s" %\
          (cols[1].text.split(".",1), cols[1].text.split(".",1), cols[1].text.split(".",2))
          #(ordem, digital_code, digital_code)
        #print ('impressao das colunas'+str(cols))

    #print digital_code
    #if 'top' in cols['valign']:
        # currency row
     #   digital_code, letter_code, units, name, rate = [c.text for c in cols]
      #  print digital_code, letter_code, units, name, rate
#soup2 = BeautifulSoup(html_doc, 'lxml')  # Parse the HTML as a string
