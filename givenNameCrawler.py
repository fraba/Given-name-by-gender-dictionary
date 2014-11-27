#!/usr/bin/env python
# encoding=utf8

## Copyright 2014 Francesco Bailo

## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

# givenNameCrawler.py

from bs4 import BeautifulSoup
import csv
import requests
import time
from time import sleep
from random import randint

# Important for UnicodeDammit
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def main():
    
    parsing_dict = {
    "male" : "http://en.wiktionary.org/wiki/Category:Male_given_names_by_language",
    "female" : "http://en.wiktionary.org/wiki/Category:Female_given_names_by_language"
    }
        
    for gender, url in parsing_dict.iteritems():
        parsePage(url, gender)
    return


def parsePage(url, gender):

    print "Parsing " + url

    try:
        html_doc = requests.get(url)
        soup = BeautifulSoup(html_doc.text)
        sleep(randint(20,30))
    except Exception,e:
        print str(e)

    if soup.find(id="mw-subcategories"):
        parseNames(soup, gender)
        urls = parseCategories(soup)
        for url in urls:
            parsePage(url, gender)
        return
        
    else:
        parseNames(soup, gender)
        return
    
        
def parseCategories(soup):

    urls = []

    for link in soup.find(id="mw-subcategories").find_all("a", href=True):
        link = link['href']
        urls.append(resolveSiteUrl(link))
    return urls
        

def parseNames(soup, gender):

    if soup.find(id="mw-pages"):

        for li in soup.find(id="mw-pages").find_all("li"):
            name = li.find("a").get_text(strip=True).encode('utf-8')
            print name
            writeName(name, gender)

        # Check whether there's another page
        for a in soup.find(id="mw-pages").find_all("a"):
            if a.get_text(strip=True)=="next 200":
                print "Parsing additional page..."
                additionalUrl = a['href']

                try:
                    html_doc = requests.get( resolveSiteUrl(additionalUrl))
                    soup = BeautifulSoup(html_doc.text)
                    # sleep(randint(20,30))
                    parseNames(soup, gender)
                except Exception,e:
                    print str(e)
                
                break
                
        
        return

    else:
        print "This category currently contains no pages."
        return


def resolveSiteUrl(link):

    url = "http://en.wiktionary.org" + link
    return url

    
def writeName(name, gender):
    
    fd = open('wiktionary_name_gender.csv','a')
    fd.write(name + "," + gender + "\n")
    fd.close()

    return

      

main()

