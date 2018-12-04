#!/usr/bin/python3

##imports
#
#
##
from bs4 import BeautifulSoup

##
#name: getURL
#para: none
#retu: string
#desc: asks user for URL link
##
def getURL():
    url=input("Enter URL: \n")
    return url
##
#name: main()
#para: none
#desc: main function to execute code
##
def main():
    url=getURL()
    print(url)
##
#name:
#para:
#desc:
##
if __name__ == "__main__":
    main()