import requests
import re
from bs4 import BeautifulSoup


#To change the site to be searched, comment the current website
#and uncomment a different website.  You can also add your own 
#website by commenting the current website in use and set url
#to a website of your choice.
#url = 'http://www.cs.txstate.edu/Personnel/jg66' 
#url = 'https://cs.txstate.edu/accounts/profiles/hs15/'
#url = 'https://cs.txstate.edu/accounts/profiles/ma04/'
url = 'https://cs.txstate.edu/accounts/profiles/mb92/'
 
def researchSpider(max_pages):
    page = 1
    while page <= max_pages:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        info = 1
        for link in soup.findAll('div', {'class': 'panel-body'}):
            title2 = link.string
            info += 1
            if info == 2:
                return title2
                
        page += 1   
        return title2
 
 
def nameSpider(max_pages):
    page = 1
    while page <= max_pages:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('h3', {'class': 'heading-title pull-left'}):
            title = link.string
        page += 1   
        return title
    
    
def educationSpider(max_pages):
    page = 1
    while page <= max_pages:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        info = 1
        for link in soup.findAll('div', {'class': 'panel-body'}):
            title2 = link.string
            info += 1
            if info == 3:
                return title2
                
        page += 1   
        return title2
    
    
    
            
            
name = nameSpider(1)

research = researchSpider(1)

education = educationSpider(1)



pattern = re.compile(r'\n')
name = re.sub(pattern, '', name)
name = ' '.join(name.split('     '))
name = ' '.join(name.split('   '))
name = ' '.join(name.split('  '))
name = ' '.join(name.split('  '))


output=open('output.txt', 'w')
output.write('Name: ')
output.write(name)
output.write('\nEducation: ')
output.write(education)
output.write('\nResearch interests: ')
output.write(research)
output.write('\nWebpage: ')
output.write(url)
output.close()



