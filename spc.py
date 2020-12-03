#!/usr/bin/python3

import pyfiglet
from bs4 import BeautifulSoup, SoupStrainer
import requests
import html2text
import argparse
import pysitemap
from usp.tree import sitemap_tree_for_homepage

import hashek


def extract_text_from_link(link):
    # TODO: handle newlines
    #   some sentences end without new line
    #   example:
    #       Bla bla bla Car
    #       Second sentence
    #       looks like:
    #       Bla bla bla CarSecond sentence
    #
    #       and hashek will then report CarSecond as error
    h = html2text.HTML2Text()

    h.ignore_links = True
    h.ignore_images = True
    h.ignore_emphasis = True

    r = requests.get(link)
    html_source = r.text

    html_text = h.handle(html_source)

    return html_text


def get_args():
    parser = argparse.ArgumentParser(
        description="Checks Croatian websites for spelling and grammar errors.")

    parser.add_argument("--url",
                        "-u",
                        action="store",
                        required=True,
                        help="Starting URL of website")

    args = parser.parse_args()

    return args.url


def print_banner():
    banner = pyfiglet.figlet_format("CroSiteSpellChecker")
    print(banner)


def main():
    print_banner()

    root_url = get_args()

    links = list()

    tree = sitemap_tree_for_homepage(root_url)

    for page in tree.all_pages():
        links.append(page.url)

    hc = hashek.Hashek()

    print("\nGathered %d links from %s" % (len(links), root_url))

    errors_fixes = list()

    for i, link in enumerate(links):
        text = extract_text_from_link(link)

        print("Checking link: %s" % link)

        suggestions_dict = hc.check_text(text)

        errors_fixes.append({link: suggestions_dict})

    hc.close()


if __name__ == '__main__':
    main()
