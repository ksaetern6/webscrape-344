#!/usr/bin/python3

##imports
#
#
##
#from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

##
#name: getURL
#para: none
#retu: string
#desc: asks user for URL link
##
def getURL():
    #url=input("Enter URL: \n")
    url=input()
    ## URL PARSER TBC
    #urlVer=urlparse(url)
    #print(urlVer)
    ##
    return url
    
##
#name: prepSoup
#para: String url
#retu: soup object
#desc: creates soup object and returns the object
##
def prepSoup(url):
    #get html page
    #rawHTML = requests.get(url).text
    #
    localLink=open("/home/ubuntu/Enviornments/webscrape/proj/craigs/htmlfile.html")
    ##
    #soup = BeautifulSoup(rawHTML,"html.parser")
    soup=BeautifulSoup(localLink.read(),'html.parser')
    
    #print(soup.prettify())
    return soup

##
#name:
#para:
#retu:
#desc:
##
def sparseData(soup):
    divList = soup.find("div", class_="content").ul
    ##for loop
    for title in divList.find_all("p", class_="result-info"): #ul -> p -> a -> text
        #a -> text
        print(title.a.text)
    return

##
#name: main()
#para: none
#retu: 
#desc: main function to execute code
##
def main():
    url=getURL()
    #print(url)
    soup=prepSoup(url)
    sparseData(soup)
    
##
#name:
#para:
#desc:
##
if __name__ == "__main__":
    main()