#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An U.S. Court of Appeals for the D.C. Circuit crawler.
"""

import json
import sys
import requests
from urlparse import urljoin
from bs4 import BeautifulSoup


OUTFILE = "results.json"
ENTRY_COUNT = 10

class USCACrawler(object):
    """
    """
    def __init__(self, amount=ENTRY_COUNT):
        self._site = "http://www.cadc.uscourts.gov/internet/opinions.nsf/OpinionsByRDate"
        self._params = "?OpenView&count=" + str(amount)
        self._url = urljoin(self._site, self._params)
        self._content = ""
        self._results = []

    def get_html(self):
        req = requests.get(self._url)
        data = req.text.decode('utf-8')
        #self._content = data
        return data

    def parse(self, content):
        soup = BeautifulSoup(content)
        entries = soup.find_all('div', {"class" : "row-entry"})[::2]
        for entry in entries:
            result = {}
            #opinion_num = entry.find("a").get_text()
            result['opinion_num'] = entry.find("span", {"class" : "column-one"}).get_text()
            result['title'] = entry.find("span", {"class" : "column-two"}).get_text()
            result['date'] = entry.nextSibling.get_text().strip()
            self._results.append(result)

        return self._results


def main():
    """
    """
    crawler = USCACrawler()
    content = crawler.get_html()
    results = crawler.parse(content)
    with open(OUTFILE, 'w') as outfile:
        json.dump(results, outfile)

if __name__ == "__main__":
    main()
    sys.exit()


