#!/usr/bin/python3
#TODO: refactor this shit, make it more modular for later website integration
from bs4 import BeautifulSoup, SoupStrainer
import requests
import html2text
import re
from sys import argv

import hashek

#url = "https://superizazov22.com/" 
#url = "https://net.hr/"
url = argv[1]
#Extract local links from website and fetch text from them
def extract_local_links_from_url(url, links):
    r = requests.get(url)
    html_source = r.text

    soup = BeautifulSoup(html_source, features="html.parser")

    for link_tag in soup.find_all('a'):
        link = link_tag.get('href')
        if (link is not None and
            link.startswith(url) and
            link != url and 
            link not in links):
            links.append(link)
            #print("link: %s" % link)
    #print("number of local links: %s" % len(links))
    #import pdb;pdb.set_trace()
    return links

links = []
links = extract_local_links_from_url(url, links)
#Recursive search of links for every link
for link in links:
    links = extract_local_links_from_url(link, links)


def extract_text_from_link(link):
    h = html2text.HTML2Text()

    h.ignore_links = True
    h.ignore_images = True
    h.ignore_emphasis = True


    r = requests.get(link)
    html_source = r.text
    html_text = h.handle(html_source)

    return html_text
    #print(html_text)
    #print("#######################################################################")

print("Found %d links!" % len(links))

for link in links:
    text = extract_text_from_link(link)
    print("Checking link: %s" % link)
    hashek.check_text(text)

